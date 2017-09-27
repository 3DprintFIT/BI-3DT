"""Uploads stuff from GitHub to Edux"""
import io
import os
import pathlib
import re
import sys
import subprocess

import easywebdav
from PIL import Image


HOST = 'edux.fit.cvut.cz'
COURSE = 'BI-3DT'
PAGES = f'/data/{COURSE}/pages/'
MEDIA = f'/data/{COURSE}/media/'

RELATIONS = {
    'schedule': 'tutorials',
    'apps': '{self}.txt',
    'admesh': 'tutorials/{self}',
    'course': 'tutorials/{self}',
    'mesh': 'tutorials/{self}',
    'reprap': 'tutorials/{self}',
    'openscad': 'tutorials/{self}',
    'slicing': 'tutorials/{self}',
    'gcode': 'tutorials/{self}',
    'slic3r': 'tutorials/{self}',
    'kisslicer': 'tutorials/{self}',
    'printing': 'tutorials/{self}',
    'bridges': 'tutorials/{self}',
    'supports': 'tutorials/{self}',
    'multicolor': 'tutorials/{self}',
    'classification': '{self}',
    'sidebar_footer': 'funding.txt',
}


class RelLinkerFakeDict(dict):
    def __missing__(self, key):
        try:
            return dokuwiki_link(key, RELATIONS[key])
        except KeyError:
            print('Warning: Cannot resolve link', key, file=sys.stderr)
            return 'deadlink'


def dokuwiki_link(key, template, separator=':'):
    link = template.format(self=key).replace('/', separator)
    if link.endswith('.txt'):
        return link[:-len('.txt')]
    return link + f'{separator}start'


def dokuwiki(path):
    """Converts given path to dokuwiki syntax, returns string"""
    return subprocess.run(('pandoc', '--to', 'dokuwiki', path),
                          universal_newlines=True, check=True,
                          stdout=subprocess.PIPE).stdout


def fix_image_links(text):
    """{{:../images/foo|bar}} -> {{:images/foo|bar}}"""
    return text.replace('../images/', 'images/')


def fix_data_links(text):
    """[[../whatnot/foo|bar]] -> {{:whatnot/foo|bar}}"""
    return re.sub(r'\[\[\.\./([^/]+)/([^\|]+)\|([^]]*)\]\]',
                  r'{{:\1/\2|\3}}', text)


def fix_relative_links(text):
    """[[./foo.md|bar]] -> [[tutorials:foo|bar]]"""
    # TODO This will break with English tutorials!
    # Also, this is very hacky :(
    text = re.sub(r'([{}])', r'\1\1', text)
    text = re.sub(r'\[\[(\./)?([^\|]+)\.md\|([^]]*)\]\]',
                  r'[[{links[\2]}|\3]]', text)
    return text.format(links=RelLinkerFakeDict())


def scale_large_images(text, maxwidth=600):
    """For each image, add ?600, but only if bigger"""
    lines = text.splitlines()
    for num, line in enumerate(lines):
        match = re.match(r'.*{{:(?P<image>[^|}]+)', line)
        if match:
            image = match.group('image').strip()
            im = Image.open(image)
            width = im.size[0]
            if width > maxwidth:
                lines[num] = re.sub(r'{{:(?P<image>[^|}]+)\|(?P<alt>[^}]+)}}',
                                    r'{{:\g<image>?' + f'{maxwidth}' +
                                    r'|\g<alt>}}',
                                    line)
    return '\n'.join(lines)


def convert(path):
    """Converts given path and runs additional functions"""
    return fix_relative_links(
        fix_data_links(scale_large_images(fix_image_links(dokuwiki(path)))))


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
    conn.upload_dir('configs', MEDIA)

    for key, value in RELATIONS.items():
        real_value = value.format(self=key)
        conn.upload_converted(f'cs/{key}.md',
                              f'{PAGES}{real_value}')
