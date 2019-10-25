#--------------------------
# Lucas Krete   <--------------------- Change this -----
# CP460 (Fall 2019)
# Midterm Student Solution File
#--------------------------

#----------------------------------------------
# You can not add any library other than these:
import math
import string
import random
import utilities
import time
#----------------------------------------------

#---------------------------------
#           Q0: Matching         #
#---------------------------------
#-------------------------------------------------------
#                   EDIT THIS FILE
# change this function such that it makes the proper matching
# Also provide your description of how you found the matching. 
#-------------------------------------------------------
def match_files():
    # Files related to vigenere cipher
    cipher1 = 'ciphertext_Lucas_Krete_q4.txt'  #<--- change this
    plain1  = 'plaintext_Lucas_Krete_q4.txt'   #<--- change this
    vigenereFiles = [plain1,cipher1]
    print('The Vigenere ciphertext file is:',cipher1)
    print("""I found that the above file is a vigenere cipher by running it through the getCipherType function that we wrote for A2.\n The function comes
to that conclusion by analyzing the character frequency as well as the chiSquared value of the ciphertext.""") #<--- complete this
    print()
    
    # Files related to substitution cipher
    cipher2 = 'ciphertext_Lucas_Krete_q3.txt'  #<--- change this
    plain2  = 'plaintext_Lucas_Krete_q3.txt'   #<--- change this
    subFiles = [plain2,cipher2]
    print('The Substitution ciphertext file is:',cipher2)
    print('I found that the above file is a substitution cipher by calculating the Index of Coincidence for the cipher.\n  I noted that it had the same IOC as english, therefore it could only be a substitution cipher.') #<--- complete this
    print()
    
    # Files related to xshift cipher
    cipher3 = 'ciphertext_Lucas_Krete_q2.txt'  #<--- change this
    plain3  = 'plaintext_Lucas_Krete_q2.txt'   #<--- change this
    xshiftFiles = [plain3,cipher3]
    print('The xshift ciphertext file is:',cipher3)
    print('''I found that the above file is an xshift cipher by running it through the getCipherType function that we wrote for A2.\n The function comes
to that conclusion by analyzing the character frequency as well as the ciSquared value of the ciphertext to determine that it is a shift cipher''') #<--- complete this
    print()
    
    # Files related to xcrypt cipher
    cipher4 = 'ciphertext_Lucas_Krete_q1.txt'  #<--- change this
    plain4  = 'plaintext_Lucas_Krete_q1.txt'   #<--- change this
    xcryptFiles = [plain4,cipher4]
    print('The xcrypt ciphertext file is:',cipher4)
    print('I found that the above file is an xcrypt cipher by mainly because it was the only cipher left, but also after coding the Xcrypt decryption algorithm,\n I got the right result and as such knew that it was a Xcrypt cipher.') #<--- complete this
    print()
    
    return [vigenereFiles,subFiles,xshiftFiles,xcryptFiles]

#---------------------------------
#         Q1: Vigenere           #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Enryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def e_vigenere(plaintext, key):
    # your code here
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return utilities.e_vigenere1(plaintext,key)
    else:
        return utilities.e_vigenere2(plaintext,key)
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def d_vigenere(ciphertext, key):
    #your code here
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (d_vigenere): invalid key!  ' + str(key))
        return ''
    key = key.lower()
    if len(key) == 1:
        return utilities.d_vigenere1(ciphertext,key)
    else:
        return utilities.d_vigenere2(ciphertext,key)
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key,plaintext
# Description:  Cryptanlysis of Vigenere Cipher (Q1)
#-----------------------------------------------------------
def cryptanalysis_vigenere(ciphertext):
    # yoru code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ''
    values=[0] * 26
    x = 0
    key_length = utilities.getKeyL_shift(ciphertext)
    #print(key_length)
    nonalpha = utilities.remove_nonalpha(ciphertext)
    blox = utilities.text_to_blocks(nonalpha,key_length)
    baskits = utilities.blocks_to_baskets(blox)
    
    #dictList = utilities.load_dictionary_modified("engmix.txt",key_length)
    #print(len(dictList))
    print("Decrypting....")
    for text in baskits:
        for x in range(26): #only 26 characters in alpha
            values[x] = utilities.get_chiSquared(utilities.d_shift(text,(x,'l')))
        index = values.index(min(values))
        key = key + alphabet[index]
    plaintext = d_vigenere(ciphertext,key)
    #i = 0
    #tupleList = []
    #for word in dictList:
        #print(str(i) + ": " + str(word))
        #print(word)
        #word.strip()
        #plaintext = d_vigenere(ciphertext, word)
        #I = utilities.get_indexOfCoin(plaintext)
        #tupleList.append(tuple((word,I)))
        #if I >= 0.063 and I <= 0.067:
            #time2 = time.time()
            #print("Decryption took: " + str(round(time2-time1)) + " seconds")
            #print(plaintext)
            #return word,plaintext
            #targetIoCIndex = i
            #targetIVal = I
        #i = i + 1
    #key = tupleList[targetIoCIndex]
    #key = key[0]
    #plaintext = d_vigenere(ciphertext,key)
    #print(plaintext)
    return key,plaintext

def comments_q1():
    print('Comments:')
    print('I discovered the key length by using the getKeyL_shift function that we wrote for the last assignment.  It proved much more reliable than a Friedman test.')  #<---- edit this
    print('''I found the keyword by exploiting our text_to_blocks and blocks_to_baskets functions.  From there I looped through each basket 26 times(since there are only 26 characters in the alphabet\n
From there, I was able to get the chi values of each basket and continually shifting it left.  From here I took the lowest chi-value index and added it to the key until I was left with a fully completed key.''')     #<---- edit this
    return

#---------------------------------
#   Q2: Substitution Cipher      #
#---------------------------------
#-------------------------------------------------------
# Parameters:   plaintext(str)
#               key: subString (str)
# Return:       ciphertext (string)
# Description:  Encryption using substitution (Q2)
#-------------------------------------------------------
def e_substitution(plaintext,key):
    # your code here
    subString = key
    subString = utilities.adjust_key(subString)
    baseString = utilities.get_baseString()
    baseString = utilities.adjust_key(baseString)
    ciphertext = ''
    for plainChar in plaintext:
        #if(plainChar == 'Ã'):
            #print(plainChar.isupper())
        if(plainChar.isupper()):
            upperFlag = True
        else:
            upperFlag = False
        plainChar = plainChar.lower()
        if plainChar in baseString:
            indx = baseString.index(plainChar)
            cipherChar = subString[indx]
            cipherChar = cipherChar.upper() if upperFlag else cipherChar
        else:
            if(upperFlag == True):
                cipherChar = plainChar.upper()
            else:
                 cipherChar = plainChar
        ciphertext += cipherChar
    #print(ciphertext)
    ciphertext = utilities.adjust_key(ciphertext)
    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: subString (str)
# Return:       plaintext (str)
# Description:  Decryption using substitution (Q2)
#-----------------------------------------
def d_substitution(ciphertext,key):
    plaintext = ""
    alphabet = utilities.adjust_key(utilities.get_baseString())
    #key = key
    
    #alphabet = utilities.adjust_key(alphabet)
    #print(alphabet)
    #print(key)
    for cipherChar in ciphertext:
        if(cipherChar.isupper()):
            upperFlag = True
        else:
            upperFlag = False
        cipherChar = cipherChar.lower()
        if cipherChar in alphabet:
            indx = key.index(cipherChar)
            plainChar = alphabet[indx]
            plainChar = plainChar.upper() if upperFlag else plainChar
        else:
            if(upperFlag == True):
                plainChar = cipherChar.upper()
            else:
                plainChar = cipherChar
        plaintext += plainChar
    #print(plaintext)
    #plaintext = utilities.adjust_key(plaintext)
    #print(utilities.adjust_key(plaintext))
    return plaintext

def cryptanalysis_substitution(ciphertext):
    #key ='''rlpdeogkvbayiucntwqhfjxsmz //,"'?;///'''
    key = '''rlpdeogkvbayiucntwqhfjxsmz ,.:"'?;!-#'''
    key = utilities.adjust_key(key)                     
    # add lines to decrypt the ciphertext
    # key is not totally correct, fix this
    plaintext = d_substitution(ciphertext,key)
    
    
    return key,plaintext

def comments_q2():
    print('Comments:')
    print('log created.  I used mainly frequency analysis, as well as some inutivite replacements to solve this. Digrams/trigrams proved very helpful!') #<----- edit this
    return

#---------------------------------
#           Q3: Xshift           #
#---------------------------------

#-----------------------------------------
# Parametes:    plaintext (str)
#               key: (shiftString,shifts)
# Return:       ciphertext (str)
# Description:  Encryption using Xshift Cipher
#-----------------------------------------
def e_xshift(plaintext, key):
    ciphertext=''
    shift_string, shift_value = key 
    shift_value = key[1] % 52

    for char in plaintext:
        if char in shift_string:
            plainindex = shift_string.index(char)
            cipherindex = (plainindex + shift_value)%52
            cipherChar = shift_string[cipherindex]
            ciphertext += cipherChar
        else:
            ciphertext += char
    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: (shiftString,shifts)
# Return:       plaintext (str)
# Description:  Decryption using Xshift Cipher
#-----------------------------------------
def d_xshift(ciphertext, key):
    plaintext=''
    shift_string, shift_value = key 
    shift_value = 52 - (key[1] % 52)
    for char in ciphertext:
        if char in shift_string:
            cipherIndex = shift_string.index(char)
            plainIndex = (cipherIndex + shift_value)%52
            plainChar = shift_string[plainIndex]
            plaintext += plainChar
        else:
            plaintext += char
    return plaintext

#-----------------------------------------
# Parametes:    ciphertext (str)
# Return:       key,plaintext
# Description:  Cryptanalysis of  Xshift Cipher
#-----------------------------------------
def cryptanalysis_xshift(ciphertext):
    #your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    atbash = alphabet[::-1]
    
    listOfData = []
    combinations = [(alphabet + alphabet.upper()),(atbash+atbash.upper()), (alphabet + atbash.upper()), (atbash + alphabet.upper())]
    
    for combo in combinations:
        i = 0
        while(i < 26):
            plain_test = d_xshift(ciphertext, tuple((combo, i)))
            chi_value = utilities.get_chiSquared(plain_test)
            listOfData.append(tuple((plain_test, chi_value, i, combo)))
            i += 1
    listOfData = sorted(listOfData, key=lambda tup:tup[1])
    for value in listOfData:
        if(utilities.is_plaintext(value[0], 'engmix.txt',0.9)):
            key = tuple((value[3], value[2]))
            plaintext = value[0]
            #print(plaintext)
            return key, plaintext
    
    return key,plaintext

def comments_q3():
    print('Comments:')
    print('Brute-force space is: 4*26 = 104 possiblities')                  #<--- edit this
    print('''I began by calculating the chi-values of each possible combination of the alphabet and atbash(lower/upper) which is 12 possibilities since once set must always be uppercase.  I noticed that
 some were redundant and this left me with 8 possiblities.  From there using the chi-values I noticed that there were repetitions...some combinations had the same chi value
 so I was able to disregard the repeated combinations and only be left with 4 possible combinations.  From here, I brute-forced my way through the remaining 4*26 possible combinations
 in order to be left with our key and correctly decrypted plaintext.  I checked if it was plaintext by utilizing our is_plaintext function we wrote on the assignment.''')   #<--- edit this
    return

#---------------------------------
#           Q4: Xcrypt           #
#---------------------------------
#-------------------------------------------------------
# Parameters:   plaintext(string)
#               key (int)
# Return:       ciphertext (string)
# Description:  Encryption using xcrypt (Q4)
#-------------------------------------------------------
def e_xcrypt(plaintext,key):
    # your code here
    r = key
    c = int(math.ceil(len(plaintext)/key))
    cipherMatrix = utilities.new_matrix(r,c,"")

    counter = 0
    for i in range(c):
        for j in range(r):
            cipherMatrix[j][i] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter+=1
    ciphertext = ""
    #utilities.print_matrix(cipherMatrix)
    for i in range(r):
        for j in range(c):
            ciphertext+=cipherMatrix[i][j]
    return ciphertext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (int)
# Return:       plaintext (string)
# Description:  Decryption using xcrypt (Q4)
#-------------------------------------------------------
def d_xcrypt(ciphertext,key):
    plaintext=''
    r = key
    c = math.ceil(len(ciphertext)/r)
    #print(c)
    #print(c)
    matrix = utilities.new_matrix(r,c,"")
    count = 0
    if(r*c != len(ciphertext)):
        return ""
    for i in range(r):
        for j in range(c):
            matrix[i][j] = ciphertext[count]
            count+=1
    #utilities.print_matrix(matrix)
    for i in range(c):
        for j in range(r):
            #if(j != c and matrix[j][i] != 'q'):
            plaintext += matrix[j][i]
    #utilities.print_matrix(matrix)
    #print(plaintext)
    flag = False
    while (flag == False):
        if plaintext[len(plaintext)-1] == 'q':
            plaintext = plaintext[:-1]
        else:
            flag = True
    
    return plaintext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key (int),plaintext (str)
# Description:  cryptanalysis of xcrypt (Q4)
#-------------------------------------------------------
def cryptanalysis_xcrypt(ciphertext):
    for i in range(1,501):
        #print("i = " + str(i))
        plaintext = d_xcrypt(ciphertext,i)
        #I = utilities.get_indexOfCoin(ciphertext)
        #print(plaintext)
        is_plain = utilities.is_plaintext(plaintext, "engmix.txt",0.8)
        #print(is_plain)
        if(is_plain == True):
            print(plaintext)
            return i, plaintext
    # your code here
    #print(plaintext)
    return i,plaintext

#-------------------------------------------------------
# Parameters:   None
# Return:       None
# Description:  Your comments on Q4 solution
#-------------------------------------------------------
def comments_q4():
    print('My Comments:')
    print('Used threshold is: 0.8',0)              # <---- edit this
    print('Cryptanalysis Method: Since there were only 500 possible keys, it makes sense to brute-force through this one. Nothing says we cant.\n So I just ran a for loop from 1-500 testing the plain text each time until I found one that was in the acceptable range.')    # <---- edit this
    return
