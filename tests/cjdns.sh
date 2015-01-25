#!/bin/bash
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

echo "Installing cjdns..."
git clone https://github.com/cjdelisle/cjdns
cd cjdns
./do

echo "Generating, cleaning conf"
./cjdroute --genconf | ./cjdroute --cleanconf > ~/cjdroute.conf
./cjdroute < ~/cjdroute.conf
python2 contrib/python/cjdnsadminmaker.py
contrib/nodejs/tools/cexec.js 'ping()'
