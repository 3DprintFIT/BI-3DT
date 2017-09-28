"""Uploads stuff from GitHub to Edux

Copyright (c) 2017 The 3D Printing Lab, Faculty of Information Technology

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

Provided license texts might have their own copyrights and restrictions

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import io
import os
import pathlib
import re
import sys
import subprocess

import click
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
    'scan': 'tutorials/{self}',
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
    'teacher': '{self}',
    'teacher/halecivo': '{self}',
    'teacher/hroncmir': '{self}',
    'teacher/prusaja3': '{self}',
    'teacher/sykorto6': '{self}',
    'teacher/wijasjan': '{self}',
    'teacher/zehramar': '{self}',
}

ASSETS = [
    'configs',
    'images',
    'stls',
]


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
        return separator + link[:-len('.txt')]
    return separator + link + f'{separator}start'


def run(*command):
    return subprocess.run(command, universal_newlines=True, check=True,
                          stdout=subprocess.PIPE).stdout


def dokuwiki(path):
    """Converts given path to dokuwiki syntax, returns string"""
    return run('pandoc', '--to', 'dokuwiki', path)


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


def _convert(path):
    """Converts given path and runs additional functions"""
    return fix_relative_links(
        fix_data_links(scale_large_images(fix_image_links(dokuwiki(path)))))


def travis_changed_files():
    commit_range = os.environ.get('TRAVIS_COMMIT_RANGE')
    if commit_range:
        return run('git', 'diff', '--name-only', commit_range).splitlines()
    return None


class Connection:
    def __init__(self, user, password):
        self.c = easywebdav.connect(HOST, username=user, password=password,
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
                self.upload_asset(path, destination + path.name)

    def upload_asset(self, path, destination):
        changed_files = travis_changed_files()
        path = str(path)
        if changed_files is None or path in changed_files:
            print('uploading', destination)
            return self.c.upload(path, destination)
        print(f'skipping {destination} (not changed)')
        return None

    def upload_converted(self, local_file, destination):
        print('converting', local_file)
        converted = io.BytesIO(_convert(local_file).encode('utf-8'))
        if not destination.endswith('.txt'):
            self.c.mkdirs(destination)
            destination = destination + '/start.txt'
        print('uploading', destination)
        self.c.upload(converted, destination)


@click.group()
def g2e():
    pass


@g2e.command()
@click.argument('markdown', nargs=-1, type=click.Path())
@click.option('--silent', is_flag=True)
def convert(markdown, silent):
    """Converts given md files to Dokuwiki, prints them to stdout"""
    for path in markdown:
        try:
            converted = _convert(path)
        except Exception:
            print(click.style(path, fg='red'))
            raise
        if silent or len(markdown) > 1:
            print(click.style(path, fg='green'))
        if not silent:
            print(converted)
            print()


@g2e.command()
@click.argument('user', envvar='EDUX_USER')
@click.argument('password', envvar='EDUX_PASSWORD')
def deploy(user, password):
    """Deploys to Edux, use EDUX_USER and EDUX_PASSWORD environment variables
    to provide credentials."""
    conn = Connection(user, password)

    for directory in ASSETS:
        conn.upload_dir(directory, MEDIA)

    for key, value in RELATIONS.items():
        real_value = value.format(self=key)
        conn.upload_converted(f'cs/{key}.md',
                              f'{PAGES}{real_value}')


if __name__ == '__main__':
    g2e()
