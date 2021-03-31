
'''
설치방법
pip install pycryptodome
테스트
python -m Crypto.SelfTest

이전버전
pip install pycryptodomex
python -m Cryptodome.SelfTest
'''
import base64
import hashlib

from Crypto import Random 
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

import time

# random = 'random'

# 사용시에는 salt라는 값을 get_private_key를 선언하면서 시스템 내부적으로 설정해주어야 한다
salt = 'sample_salt'


# def __init__(self):
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-s[-1]]
key = PBKDF2(random, salt, 64, 1000)[:32]
        
def get_private_key(random):
#     salt 선언은 여기서
#     salt = my_settings.SECRET.get('salt')
    kdf = PBKDF2(random, salt, 64, 1000)
    key = kdf[:32]
    return key

#random 값은 개인키 값으로 암호화 복호화를 사용하면서 계속해서 넣어줄 값이다
def encrypt(raw, random):
    private_key = get_private_key(random)
    raw = pad(raw).encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
    
def decrypt(enc, random):
    private_key = get_private_key(random)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
    
def encrypt_str(raw):
    return encrypt(raw).decode('utf-8')

def decrypt_str(enc):
    if type(enc) == str:
        enc = str.encode(enc)
    return decrypt(enc).decode('utf-8')
