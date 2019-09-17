def getMode() :
    while True :
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split() :
            return mode
        else :
            print('The value you entered its invalid')

def getFileName() :
    print('Enter your file name : ')
    return input()

def getKey() :
    key = ""
    while True :
        print('Enter the key : ')
        return input()
    
def encrypt_decrypt(mode , fileName, key) :
    outputFileName = 'encrypt.txt'
    if mode[0] == 'd' :
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = open(outputFileName , 'w')
    
    inputFile = open(fileName , 'r')
    message = inputFile.read()
    
    idx = 0 
    for symbol in message :
        translated += vigenere(symbol, idx , mode)
        idx += 1
    
    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    
def vigenere(symbol, idx , mode) :
    add_key = 0
    
    if ord(symbol) >= 97 and ord(symbol) <= 122 :
        add_key = 97
        target_ascii = ord(symbol) - add_key  # 0 ~ 25

    else :
        add_key = 65
        target_ascii = ord(symbol) - add_key
    
    
    if ord(key[idx % len(key)]) >= 97 and ord(key[idx % len(key)]) <= 122 :
        key_ascii = ord(key[idx % len(key)]) - 97 
    else : 
        key_ascii = ord(key[idx % len(key)]) - 65
    
    if mode[0] =='d' : 
        if target_ascii - key_ascii >= 0 :
            change_ascii = (target_ascii - key_ascii) + add_key
        else : 
            change_ascii = 26 + (target_ascii - key_ascii ) + add_key 
    else:
        change_ascii = ((target_ascii  + key_ascii ) % 26 ) + add_key 
        
    return chr(change_ascii)


mode = getMode()
key = getKey()
fileName = getFileName()
encrypt_decrypt(mode, fileName ,key)