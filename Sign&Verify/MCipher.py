from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import base64
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

BS = 16
pad = lambda s : s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s) -1:])]

def setAES(key , iv) :
    return AES.new(key , AES.MODE_CBC, iv)

def AES_Encrypt(cipher , data) :
        pad_message = pad(data)   
        pad_message_encode = pad_message.encode()
        encrpyt_pad_message_encode = cipher.encrypt(pad_message_encode)
        enc_message = base64.b64encode(encrpyt_pad_message_encode)
        return enc_message

def AES_Decrypt(cipher, data ):
    decode_message = base64.b64decode(data)
    decrpyt_meesage = cipher.decrypt(decode_message)
    dec_message = unpad(decrpyt_meesage).decode()
    return dec_message

def readPEM(filename) :
    f = open(filename,"r")
    key = RSA.importKey(f.read())
    f.close()
    return key

def RSAEncrypt(pubkey , data) :
    return pubkey.encrypt(data.encode() , 32)

def RSADecrypt(prikey, data) :
    return prikey.decrypt(data).decode()


def makeHashBlock(data, key) :
    hasher = SHA256.new(data.encode())
    signature = sign(key, hasher)
    sign_decode = base64.b64encode(signature).decode()
    block = '{0:04x}'.format(len(data))+ data + '{0:04x}'.format(len(sign_decode)) + sign_decode
    return block


def separateHashBlcok(Block) :
    data_size = int(Block[:4],16)
    data = Block[4:data_size+4]
    signdata_size = int(Block[data_size+4:data_size+4+4],16)
    signData = Block[data_size+4+4 :]
    return data , base64.b64decode(signData)



def sign(priKey, hashData) : 
    signer = PKCS1_v1_5.new(priKey)
    signature = signer.sign(hashData)
    return signature

def verify(pubKey, message, signData) : 
    verifier = PKCS1_v1_5.new(pubKey)
    hasher = SHA256.new(message.encode())
    if verifier.verify(hasher, signData) :
        return True
    else :
        return False




