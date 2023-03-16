import sys

from gvm.connections import UnixSocketConnection
from gvm.errors import GvmError
from gvm.protocols.gmpv224 import Gmp
from gvm.transforms import EtreeCheckCommandTransform

path = '/tmp/gvm/gvmd/gvmd.sock'
connection = UnixSocketConnection(path=path)
transform = EtreeCheckCommandTransform()

nome = 'teste1'
ports = '33d0cd82-57c6-11e1-8ed1-406186ea4fc5'

try:

    with Gmp(connection=connection, transform=transform) as gmp:
        gmp.authenticate('admin', 'admin')
        
        gmp.create_target(name=nome, hosts='192.168.0.1, 192.168.0.2', port_list_id=ports)

except GvmError as e:
    print('An error occurred', e, file=sys.stderr)
