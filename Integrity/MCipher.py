import hashlib
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



def sha256(data) :
    return hashlib.sha256(data.encode()).hexdigest()

def makeHashBlock(data) :
    hashdata = sha256(data)
    hashblock = '{0:04x}'.format(len(data))+ data + '{0:04x}'.format(len(hashdata)) + hashdata
    return hashblock

def separateHashBlcok(hashBlock) :
    data_size = int(hashBlock[:4],16)
    data = hashBlock[4:data_size+4]
    hashdata_size = int(hashBlock[data_size+4:data_size+4+4],16)
    hashData = hashBlock[data_size+4+4 :data_size+4+4 +hashdata_size]
    return data ,hashData

def integrityCheck(data, hashData) :
    data_hash = sha256(data)
    if data_hash == hashData :
        return True
    else : 
        return False
