import sys
from lxml import etree
from gvm.connections import UnixSocketConnection
from gvm.errors import GvmError
from gvm.protocols.gmpv224 import Gmp
from gvm.transforms import EtreeCheckCommandTransform

path = '/tmp/gvm/gvmd/gvmd.sock'
connection = UnixSocketConnection(path=path)
transform = EtreeCheckCommandTransform()

try:

    with Gmp(connection=connection, transform=transform) as gmp:
        gmp.authenticate('admin', 'admin')
        
        targets = gmp.get_targets()

        formatted = etree.tostring(etree.fromstring(targets), pretty_print=True).decode()

        print(formatted)
                     
except GvmError as e:
    print('An error occurred', e, file=sys.stderr)
