import sys

from gvm.connections import UnixSocketConnection
from gvm.errors import GvmError
from gvm.protocols.gmpv224 import Gmp
from gvm.transforms import EtreeCheckCommandTransform

path = '/tmp/gvm/gvmd/gvmd.sock'
connection = UnixSocketConnection(path=path)
transform = EtreeCheckCommandTransform()

id = 'um id qualquer'
port_ranges = {}

try:

    with Gmp(connection=connection, transform=transform) as gmp:
        gmp.authenticate('admin', 'admin')

        port_config = gmp.get_port_list('id')

        for element in port_config[0].iter("start", "end"):
            port_ranges[element.getparent().attrib.get("id")] = {}
            port_ranges[element.getparent().attrib.get("id")][element.tag] = {element.text}

except GvmError as e:
    print('An error occurred', e, file=sys.stderr)
