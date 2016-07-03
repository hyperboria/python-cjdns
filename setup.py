#!/usr/bin/env python
# You may redistribute this program and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Basic setup.py file to install and README from markdown to rst"""


from setuptools import setup
import os


def readme(fname):
    """Reads a markdown file and returns the contents formatted as rst"""
    md = open(os.path.join(os.path.dirname(__file__), fname)).read()
    output = md
    try:
        import pypandoc
        output = pypandoc.convert(md, 'rst', format='md')
    except ImportError:
        pass
    return output

setup(
    name='cjdns',
    version='0.2.4',
    description='A library to interact with the cjdns Admin Interface',
    long_description=readme('README.rst'),
    url='https://github.com/hyperboria/python-cjdns',
    bugtracker_url='https://github.com/hyperboria/python-cjdns/issues',
    author='Finn Herzfeld',
    author_email='finn@seattlemesh.net',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Topic :: System :: Networking'
    ],
    keywords='cjdns',
    packages=['cjdns'],
    scripts=['util/cexec', 'util/peerStats'],
    install_requires=[
        'prettytable'
    ]
)
