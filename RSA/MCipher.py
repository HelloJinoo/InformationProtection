from Crypto.Cipher import AES
import base64
from Crypto.PublicKey import RSA

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
    dec_message = unpad(decrpyt_meesage).decode('utf-8')
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
    