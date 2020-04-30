from ctypescrypto.engine import Engine,set_default
from ctypescrypto.cms import SignedData,Flags
from ctypescrypto.pkey import PKey
from ctypescrypto.x509 import X509

set_default(Engine('gost'))


req = """data to sign"""

with open('/home/eri/Projects/rkn/provider.pem','rb') as f:
    d = f.read()

cert = X509(d) # сертификат с приватным ключем в формате pem в переменной d, загружаю сертификат
p = cert.pubkey

pk = PKey(privkey=d) # приватный ключ

mes = SignedData.create(req, cert, pk, flags=Flags.DETACHED+Flags.BINARY)

with open('req.txt.sig','wb') as f:
    f.write(mes.pem())

with open('req.txt','wb') as f:
    f.write(req)
