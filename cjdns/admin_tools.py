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

def whoami(cjdns):
    from .key_utils import to_ipv6

    res = cjdns.NodeStore_nodeForAddr(0)
    key = res['result']['key']
    ver = res['result']['protocolVersion']
    IP6 = to_ipv6(key)

    return {'IP': IP6, 'key': key, 'version': ver}
