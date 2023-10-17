import hashlib
import math
sha256 = hashlib.sha256()
####### parameter
rb = 'device'.encode('utf-8')
IDi = 'hung123'.encode('utf-8')
PW = '123hung'.encode('utf-8')
Bio = 'vantay'.encode('utf-8')


def int_to_bytes(integer_in: int) -> bytes:
    """Convert an integer to bytes"""
    # Calculates the least amount of bytes the integer can be fit into
    length = math.ceil(math.log(integer_in) / math.log(256))

    return integer_in.to_bytes(length, 'little')

def interger(value):

    return int.from_bytes(value, byteorder='big', signed=False)

def private_key(IDi,PW,Bio,rb):
    value = int_to_bytes(interger(IDi+PW)^interger(Bio+rb))
    sha256.update(value)
    return sha256.digest()

i = private_key(IDi,PW,Bio,rb)