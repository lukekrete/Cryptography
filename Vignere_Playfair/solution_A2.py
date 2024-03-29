#--------------------------
# Luke Krete 160758350
# CP460 (Fall 2019)
# Assignment 2
#--------------------------

import math
import string
import utilities_A2

#---------------------------------
#Q1: Vigenere Cipher (Version 2) #
#---------------------------------
#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): string of any length
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call e_vigenere1
#               else --> call e_vigenere2
#               If invalid key (not string or empty string or non-alpha string) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def e_vigenere(plaintext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return e_vigenere1(plaintext,key)
    else:
        return e_vigenere2(plaintext,key)

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): string of anylength
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call d_vigenere1
#               else --> call d_vigenere2
#               If invalid key (not string or empty string or contains no alpha char) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def d_vigenere(ciphertext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (d_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return d_vigenere1(ciphertext,key)
    else:
        return d_vigenere2(ciphertext,key)

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere1(plaintext, key):
    square = utilities_A2.get_vigenereSquare()
    ciphertext = ''
    for char in plaintext:
        if char.lower() in square[0]:
            plainIndex = square[0].index(char.lower())
            keyIndex = square[0].index(key)
            cipherChar = square[keyIndex][plainIndex]
            ciphertext+= cipherChar.upper() if char.isupper() else cipherChar
            key = char.lower()
        else:
            ciphertext += char
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere2(plaintext, key):
    square = utilities_A2.get_vigenereSquare()
    ciphertext = ''
    counter = 0
    for char in plaintext:
        if char.lower() in square[0]:
            plainIndex = square[0].index(char.lower())
            keyIndex = square[0].index(key[counter%len(key)])
            cipherChar = square[keyIndex][plainIndex]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            counter += 1
        else:
            ciphertext += char
    return ciphertext
    
#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere1(ciphertext, key):
    square = utilities_A2.get_vigenereSquare()
    plaintext = ''
    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndex = square[0].index(key)
            plainIndex = 0
            for i in range(26):
                if square[i][keyIndex] == char.lower():
                    plainIndex = i
                    break
            plainChar = square[0][plainIndex]
            key = plainChar
            plaintext += plainChar.upper() if char.isupper() else plainChar
        else:
            plaintext += char
    return plaintext

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere2(ciphertext, key):
    square = utilities_A2.get_vigenereSquare()
    plaintext = ''
    counter = 0
    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndex = square[0].index(key[counter%len(key)])
            plainIndex = 0
            for i in range(26):
                if square[i][keyIndex] == char.lower():
                    plainIndex = i
                    break
            plainChar = square[0][plainIndex]
            plaintext += plainChar.upper() if char.isupper() else plainChar
            counter += 1
        else:
            plaintext += char
    return plaintext


#-------------------------------------
#Q2: Vigenere Crytanalysis Utilities #
#-------------------------------------

#-----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
#------------------------------------------------------------------------------
def text_to_blocks(text,size):
    # your code here
    blocks = []
    for i in range(0,len(text),size):
        blocks.append(text[i:i+size])
    return blocks

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
#-----------------------------------
def remove_nonalpha(text):
    modifiedText = ''
    for char in text:
        if char.isalpha():
            modifiedText+=char.upper()
    return modifiedText

#-------------------------------------------------------------------------------------
# Parameters:   blocks: list of strings
# Return:       baskets: list of strings
# Description:  Assume all blocks have same size = n (other than last block)
#               Create n baskets
#               In basket[i] put character #i from each block
#---------------------------------------------------------------------------------------
def blocks_to_baskets(blocks):
    baskets = [""] * len(blocks[0])
    for block in blocks:
        for i in range(len(block)):
            baskets[i]+=block[i]
    return baskets

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       I (float): Index of Coincidence
# Description:  Computes and returns the index of coincidence 
#               for a given text
#----------------------------------------------------------------
def get_indexOfCoin(ciphertext):
    # your code here
    I = 0
    cipherSet = list(set(ciphertext))
    arr = [0] * len(cipherSet)
    for i in range(len(cipherSet)):
        for key in ciphertext:
            if(cipherSet[i] == key):
                arr[i] +=1
    if(len(arr) > 0):
        for i in range(len(arr)):
            I = I + (arr[i] / len(ciphertext)) * (((arr[i]) - 1) / (len(ciphertext)-1))
    else:
        I = 0
    return I

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses Friedman's test to compute key length
#               returns key length rounded to nearest integer
#---------------------------------------------------------------
def getKeyL_friedman(ciphertext):
    # your code here
    n = len(ciphertext)
    I = get_indexOfCoin(ciphertext)
    k = math.ceil((0.027 * n)/((n-1)*I+0.065-0.038*n))
    return k

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    # your code here
    #No idea how to do this Quitaiba
    k = 0
    return k
#---------------------------------
#   Q3:  Block Rotate Cipher     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (b,r)
# Return:       updatedKey (b,r)
# Description:  Assumes given key is in the format of (b(int),r(int))
#               Updates the key in three scenarios:
#               1- The key is too big (use modulo)
#               2- The key is negative
#               if an invalid key is given print error message and return (0,0)
#-----------------------------------------------------------
def adjustKey_blockRotate(key):
    updatedKey = ()
    error = 'Error (adjustKey_blockRotate): Invalid key'
    if type(key) is tuple:
        b=key[0]
        r=key[1]
        if b > 0:
            if type(b) is int and type(r) is int:
                updatedKey = (b,(r%b))
            else:
                print(error,end='')
                updatedKey = (0,0)
        else:
            print(error,end='')
            updatedKey = (0,0)      
    else:
        print(error,end='')
        updatedKey = (0,0)     
    return updatedKey

#-----------------------------------
# Parameters:   text (string)
# Return:       nonalphaList (2D List)
# Description:  Analyzes a given string
#               Returns a list of non-alpha characters along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#               Example: get_nonalpha('I have 3 cents.') -->
#                   [[' ', 1], [' ', 6], ['3', 7], [' ', 8], ['.', 14]]
#-----------------------------------
def get_nonalpha(text):
    # your code here
    nonalphaList=[]
    for i in range(len(text)):
        if(text[i].isalpha() == False):
            temp = [text[i],i]
            nonalphaList.append(temp)
    return nonalphaList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_nonalpha(text, nonAlpha):
    # your code here
    modifiedText = text
    if(len(nonAlpha)>0):
        for i in range(len(nonAlpha)):
            modifiedText = modifiedText[:nonAlpha[i][1]] + nonAlpha[i][0] + modifiedText[nonAlpha[i][1]:]
    return modifiedText

#-----------------------------------------------------------
# Parameters:   plaintext (string)
#               key (b,r): (int,int)
# Return:       ciphertext (string)
# Description:  break plaintext into blocks of size b
#               rotate each block r times to the left
#-----------------------------------------------------------
def e_blockRotate(plaintext,key):
    # your code here
    nonAlpha = get_nonalpha(plaintext)
    ciphertext =''
    plaintext = "".join([char for char in plaintext if char.isalpha()])
    blocks = text_to_blocks(plaintext, key[0])
    for _ in range(len(blocks[len(blocks)-1]),len(blocks[0]), 1):
        blocks[len(blocks)-1]+= 'q'
    for block in blocks:
        ciphertext += utilities_A2.shift_string(block, key[1], 'l')
    ciphertext = insert_nonalpha(ciphertext, nonAlpha)
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               key (b,r): (int,int)
# Return:       plaintext (string)
# Description:  Decryption using Block Rotate Cipher
#-----------------------------------------------------------
def d_blockRotate(ciphertext,key):
    # your code here
    plaintext = ''
    nonAlpha = get_nonalpha(ciphertext)
    ciphertext = "".join([char for char in ciphertext if char.isalpha()])
    blocks = text_to_blocks(ciphertext, key[0])

    for i in range(len(blocks)):
        blocks[i] = utilities_A2.shift_string(blocks[i], key[1], 'r')
        #print(blocks[i])
    temp = ''
    for letter in blocks[len(blocks)-1]:
        if(letter != 'q'):
            temp += letter
    blocks[len(blocks)-1] = temp
    for block in blocks:
        for j in range(len(block)):
            plaintext+= block[j]
    plaintext = insert_nonalpha(plaintext, nonAlpha)
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               b1 (int): starting block size
#               b2 (int): end block size
# Return:       plaintext,key
# Description:  Cryptanalysis of Block Rotate Cipher
#               Returns plaintext and key (r,b)
#               Attempts block sizes from b1 to b2 (inclusive)
#               Prints number of attempts
#-----------------------------------------------------------
def cryptanalysis_blockRotate(ciphertext,b1,b2):
    # your code here
    plaintext=''
    key = (0,0)
    attempts = 0
    for blockSize in range(b1,b2,1):
        for possibleKey in range(1, blockSize,1):
            text = d_blockRotate(ciphertext, (blockSize,possibleKey))
            if (utilities_A2.is_plaintext(text, 'engmix.txt', 0.9)):
                plaintext = text
                key = (blockSize, possibleKey)
                print("Key found after", attempts+1, " attempts")
                print("Key = ", key)
                print("Plaintext:",plaintext)
                return plaintext, key
            attempts+=1
    print("Block Rotate Cryptanalysis Failed. No Key was found")
    return plaintext,key

#---------------------------------
#       Q4: Cipher Detector     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   ciphertext (string)
# Return:       cipherType (string)
# Description:  Detects the type of a given ciphertext
#               Categories: "Atbash Cipher, Spartan Scytale Cipher,
#                   Polybius Square Cipher, Shfit Cipher, Vigenere Cipher
#                   All other ciphers are classified as Unknown. 
#               If the given ciphertext is empty return 'Empty Ciphertext'
#-----------------------------------------------------------
def get_cipherType(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not ciphertext.strip():
        return "Empty Ciphertext"
    cipherType = ""
    only_text = remove_nonalpha(ciphertext)
    if (only_text == ""):
        cipherType = "Polybius Square Cipher"
        return cipherType
    chiSquared = (utilities_A2.get_chiSquared(ciphertext))
    if(chiSquared < 400):
        cipherType = "Spartan Scytale Cipher"
        return cipherType
    else: 
        i = (get_indexOfCoin(ciphertext))
        if (i > 0.062 and i < 0.068):
            flipped_cipher = ""
            for c in only_text:
                flipped_cipher += alphabet[25 - alphabet.index(c)]
            flipped_Chi = utilities_A2.get_chiSquared(flipped_cipher)
            if (flipped_Chi < 150):
                cipherType = "Atbash Cipher"
                return cipherType
            else:
                cipherType = "Shift Cipher"
                return cipherType
        elif (i > 0.0415 and i < 0.062):
            cipherType = "Vigenere Cipher"
            return cipherType 
        else:
            cipherType = "Unknown Cipher"
            return cipherType            
    return cipherType

#-------------------------------------
#  Q5: Wheastone Playfair Cipher     #
#-------------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (string)
# Return:       modifiedPlain (string)
# Description:  Modify a plaintext through the following criteria
#               1- All non-alpha characters are removed
#               2- Every 'W' is translsated into 'VV' double V
#               3- Convert every double character ## to #X
#               4- if the length of text is odd, add X
#               5- Output is formatted as pairs, separated by space
#                   all upper case
#-----------------------------------------------------------
def formatInput_playfair(plaintext):
    plaintext = plaintext.upper()
    modifiedPlain = ""
    i = 1
    for char in plaintext:
        if char.isalpha():
            if char == 'W' and modifiedPlain[-1] == ' ':
                modifiedPlain+='VX'
                i+=1
            elif char == 'W' and modifiedPlain[-1] != ' ':
                modifiedPlain+='V V'
                i+=1
            elif modifiedPlain!= '' and char == modifiedPlain[-1]:
                modifiedPlain+='X'
            else: 
                modifiedPlain = modifiedPlain + char
        if i%2 == 0 and i!=0:
            modifiedPlain+=' '
        if char!= ' ':
            i+=1
    if i%2==0:
        modifiedPlain +='X'
    return modifiedPlain

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Encryption using Wheatstone Playfair Cipher
#---------------------------------------------------------------------------------------
def e_playfair(plaintext, key):
    ciphertext=''
    newtext=formatInput_playfair(plaintext)
    for index in range(0,len(newtext), 3):
        c1 = newtext[index]
        c2 = newtext[index+1]
        i = 0
        for list in key:
            if c1 in list:
                i1 = i
                j1=list.index(c1)
            if c2 in list:
                i2 = i
                j2 = list.index(c2)
            i+=1     
        ciphertext += e_playfair_sub(i1,j1,i2,j2,key)
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   i1 (int)
#		i2(int)
#		j1/j2 (int)
#		key (2D list)	
# Return:       ciphertext (string)
# Description:  helper function for encrypting via playfair cipher
#---------------------------------------------------------------------------------------

def e_playfair_sub(i1,j1,i2,j2,key):
    ciphertext = ''
    if (i1==i2):
        j1=(j1+1)%5
        j2=(j2+1)%5
        ciphertext += key[i1][j1]+ key[i2][j2]+' '
    elif(j1 == j2):
        ciphertext += key[(i1+1)%5][j1]+ key[(i2+1)%5][j2]+' '
    else:
        ciphertext +=key[i1][j2]+key[i2][j1]+' '
    return ciphertext
#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Decryption using Wheatstone Playfair Cipher
#-------------------------------------------------------------------------------
def d_playfair(ciphertext, key):
    plaintext = ''
    for index in range(0, len(ciphertext), 3):
        c1 = ciphertext[index]
        c2 = ciphertext[index+1]
        i=0
        for list in key:
            if c1 in list:
                i1 = i
                j1 = list.index(c1)
            if c2 in list:
                i2 = i
                j2 = list.index(c2)
            i+=1
        plaintext += d_playfair_sub(i1,j1,i2,j2,key)
    return plaintext


#-------------------------------------------------------------------------------------
# Parameters:   i1 (int)
#		i2(int)
#		j1/j2 (int)
#		key (2D list)	
# Return:       plaintext (string)
# Description:  helper function for decrypting via playfair cipher
#---------------------------------------------------------------------------------------
def d_playfair_sub(i1,j1,i2,j2,key):
    plaintext = ''
    if (i1==i2):
        j1=(j1-1)%5
        j2=(j2-1)%5
        plaintext += key[i1][j1]+ key[i2][j2]+' '
    elif(j1 == j2):
        plaintext += key[(i1-1)%5][j1]+ key[(i2-1)%5][j2]+' '
    else:
        plaintext +=key[i1][j2]+key[i2][j1]+' '
    return plaintext