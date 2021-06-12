#cifrar valores con sha 256 y typestring byte

import hashlib

h=haslib.sha256()

h.update(b"salty8257devnet_password")

hash = h.hexdigest()

pring(hash)
