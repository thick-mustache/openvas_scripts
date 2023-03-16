from gvm.protocols import gmp

status = gmp.getversion().get('status')

print(status)
