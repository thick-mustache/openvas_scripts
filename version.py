import sys

from gvm.connections import UnixSocketConnection
from gvm.errors import GvmError
from gvm.protocols.gmpv224 import Gmp
from gvm.transforms import EtreeCheckCommandTransform

path = '/tmp/gvm/gvmd/gvmd.sock'
connection = UnixSocketConnection(path=path)
transform = EtreeCheckCommandTransform()

try:

    with Gmp(connection=connection, transform=transform) as gmp:

        version = gmp.get_version()

        print(version[0].text)

except GvmError as e:
    print('An error occurred', e, file=sys.stderr)
