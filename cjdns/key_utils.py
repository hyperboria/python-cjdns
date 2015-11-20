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

from hashlib import sha512

from . import base32


def to_ipv6(key):
    """Get IPv6 address from a public key."""

    if key[-2:] != '.k':
        raise ValueError('Key does not end with .k')

    key_bytes = base32.decode(key[:-2])
    hash_one = sha512(key_bytes).digest()
    hash_two = sha512(hash_one).hexdigest()

    return ':'.join([hash_two[i:i+4] for i in range(0, 32, 4)])
