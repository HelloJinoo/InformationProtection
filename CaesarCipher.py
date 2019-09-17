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

    
MAX_KEY_SIZE = 26
def caesar_getKey() :
    key = 0 
    while True :
        print("Enter ther key Number (1-%s)" % (MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE :
            return key
        
def caesar(symbol, key, mode) :
    target_ascii = ord(symbol)
    add_ascii = 0 
    
    if target_ascii >= 97 and target_ascii <= 122 :
        add_ascii = 97
        target_ascii = target_ascii - add_ascii    #0 ~ 25
 
    else : 
        add_ascii = 65
        target_ascii = target_ascii - add_ascii
        

    if mode[0] =='d' : 
        if target_ascii + key >= 0 :
            change_ascii = (( target_ascii + key ) ) + add_ascii #Encoding or Decoding  %26
        else : 
            change_ascii = 26 + (target_ascii + key ) + add_ascii #Encoding or Decoding 
    else:
        change_ascii = ((target_ascii + key ) % 26 ) + add_ascii #Encoding or Decoding   
 
    return chr(change_ascii)


def caesar_encrypt(mode , fileName, key) :
    outputFileName = 'encrypt.txt'
    if mode[0] == 'd' :
        key = -key
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = open(outputFileName , 'w')
    
    inputFile = open(fileName , 'r')
    message = inputFile.read()
    
    for symbol in message :
        translated += caesar(symbol, key , mode)

    
    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    
mode = getMode()
key = caesar_getKey()
fileName = getFileName()
caesar_encrypt(mode, fileName ,key)
    