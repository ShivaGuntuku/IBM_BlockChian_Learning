from hashlib import sha256
data = "Some variable length data"
print (sha256(data.encode('utf-8')).hexdigest())