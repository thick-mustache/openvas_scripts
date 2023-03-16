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
        gmp.authenticate('admin', 'admin')
        
        targets = gmp.get_targets()
            
    for target in targets:
        print("Target:")
        for key, value in target.items():
            if isinstance(value, list):
                print(f"\t{key}:")
                for subvalue in value:
                    print(f"\t\t{subvalue}")
            else:
                print(f"\t{key}: {value}")

except GvmError as e:
    print('An error occurred', e, file=sys.stderr)
