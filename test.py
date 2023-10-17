import hashlib

# Your bytes data
data_bytes = b'\x02\r\x1c\x1eVVHRF_\x06\x18uh'

# Create a SHA-256 hash object
sha256 = hashlib.sha256()

# Update the hash object with your bytes data
sha256.update(data_bytes)

# Get the hash value as a bytes object
hashed_bytes = sha256.digest()

print("SHA-256 hash as bytes:", hashed_bytes)
