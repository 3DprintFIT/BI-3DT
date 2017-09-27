"""Uploads stuff from GitHub to Edux"""
import io
import os
import pathlib
import re
import subprocess

import easywebdav


HOST = 'edux.fit.cvut.cz'
COURSE = 'BI-3DT'
PAGES = f'/data/{COURSE}/pages/'
MEDIA = f'/data/{COURSE}/media/'


def dokuwiki(path):
    """Converts given path to dokuwiki syntax, returns string"""
    return subprocess.run(('pandoc', '--to', 'dokuwiki', path),
                          universal_newlines=True, check=True,
                          stdout=subprocess.PIPE).stdout


def fix_image_links(text):
    """{{:../images/foo|bar}} -> {{:images/foo|bar}}"""
    return text.replace('../images/', 'images/')


def fix_stl_links(text):
    """[[../stls/foo|bar]] -> {{:stls/foo|bar}}"""
    return re.sub(r'\[\[\.\./stls/([^\|]+)\|([^]]*)\]\]',
                  r'{{:stls/\1|\2}}', text)


def fix_relative_links(text):
    """[[./foo.md|bar]] -> [[tutorials:foo|bar]]"""
    # TODO This will break with English tutorials!
    return re.sub(r'\[\[(\./)?([^\|]+)\.md\|([^]]*)\]\]',
                  r'[[tutorials:\2|\3]]', text)


def convert(path):
    """Converts given path and runs additional functions"""
    return fix_relative_links(fix_stl_links(fix_image_links(dokuwiki(path))))


class Connection:
    def __init__(self):
        self.c = easywebdav.connect(HOST,
                                    username=os.environ['EDUX_USER'],
                                    password=os.environ['EDUX_PASSWORD'],
                                    protocol='https')

    def upload_dir(self, local_directory, destination):
        local_directory = pathlib.Path(local_directory)
        dirname = local_directory.name
        destination = destination + dirname + '/'
        print('creating', destination)
        self.c.mkdirs(destination)
        for path in local_directory.iterdir():
            if path.is_dir():
                self.upload_dir(path, destination)
            else:
                print('uploading', destination + path.name)
                self.c.upload(str(path), destination + path.name)

    def upload_converted(self, local_file, destination):
        print('converting', local_file)
        converted = io.BytesIO(convert(local_file).encode('utf-8'))
        if not destination.endswith('.txt'):
            self.c.mkdirs(destination)
            destination = destination + '/start.txt'
        print('uploading', destination)
        self.c.upload(converted, destination)


if __name__ == '__main__':
    conn = Connection()
    conn.upload_dir('images', MEDIA)
    conn.upload_dir('stls', MEDIA)

    for tutorial in ('admesh', 'course', 'mesh', 'reprap',
                     'openscad', 'slicing', 'gcode', 'slic3r'):
        conn.upload_converted(f'cs/{tutorial}.md',
                              f'{PAGES}tutorials/{tutorial}')
