#--------------------------
# Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Midterm Student Utilities File
#--------------------------

#-----------------------------------------------
# Remember to change the name of the file to:
#               utilities.py
# Delete this box after changing the file name
# ----------------------------------------------

#----------------------------------------------
# You can not add any library other than these:
import math
import string
import random
import solution
#----------------------------------------------

#-----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName,'r')
    contents = inFile.read()
    inFile.close()
    return contents

#-----------------------------------------------------------
# Parameters:   None
# Return:       baseString (str)
# Description:  Returns base string for substitution cipher
#-----------------------------------------------------------
def get_baseString():
    #generate alphabet
    alphabet = ''.join([chr(ord('a')+i) for i in range(26)])    
    symbols = """.,; #"?'!:-"""     #generate punctuations
    return alphabet + symbols

#-----------------------------------------------------------
# Parameters:   key (str)
# Return:       key (str)
# Description:  Utility function for Substitution cipher
#               Exchanges '#' wiht '\n' and vice versa
#-----------------------------------------------------------
def adjust_key(key):
    if '#' in key:
        newLineIndx = key.index('#')
        key = key[:newLineIndx]+'\n'+key[newLineIndx+1:]
    else:
        newLineIndx = key.index('\n')
        key = key[:newLineIndx]+'#'+key[newLineIndx+1:]
    return key

# you can add any utility functions as you like



# Included Functions
#   1- file_to_text(fileName)
#   2- text_to_file(fileName)
#   3- get_lower()
#   4- get_vigenereSquare()
#   5- get_freqTable()
#   6- get_charCount(text)
#   7- shift_string(s,n,d)
#   8- get_chiSquared(text)
#   9- load_dictionary(dictFile)
#   10- text_to_words(text)
#   11- analyze_text(text, dictFile)
#   12- is_plaintext(text, dictFile, threshold)
#   13- e_shift(plaintext,key)
#   14- d_shift(ciphertext,key)
#   15- cryptanalysis_shift(ciphertext)
#   16- get_playfairSquare()


def text_to_blocks(text,size):
    # your code here
    blocks = []
    for i in range(0,len(text),size):
        blocks.append(text[i:i+size])
    return blocks

def blocks_to_baskets(blocks):
    baskets = [""] * len(blocks[0])
    for block in blocks:
        for i in range(len(block)):
            baskets[i]+=block[i]
    return baskets

#function for troupleshooting the substitution cipher
def compare():
    #alphabet = """poejiqsrbltxwaznfcdhmvgkuy:'" !.?,-#;"""
    #print(get_baseString())
    #print(alphabet)
    #alphabet = adjust_key(alphabet)
    var1 = file_to_text("plaintext_xcrypt_sample.txt")
    print(var1)
    var2 = solution.d_xcrypt(file_to_text("ciphertext_xcrypt_sample.txt"),82)
    print(var2)
    #var3 = file_to_text("plaintext_subcipher_sample.txt")
    #print(len(var2))
    #print(var2)
    #print(var3[1073])
    #print(var2)
    for i in range(len(var2)):
        if var1[i] != var2[i]:
            print("var1 is: " + var1[i] + "var2 is: " + var2[i])
            print(i)

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere1(plaintext, key):
    square = get_vigenereSquare()
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
    square = get_vigenereSquare()
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
    square = get_vigenereSquare()
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
    square = get_vigenereSquare()
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

def is_plaintext(text, dictFile, threshold):
    if(threshold < 0 or threshold > 1):
        threshold = 0.9
    matches, mismatches = analyze_text(text,dictFile)
    if(matches >0 and mismatches >= 0):
        if ((matches/(matches + mismatches)) >= threshold):
            return True
    # your code here
    return False

def remove_nonalpha(text):
    modifiedText = ''
    for char in text:
        if char.isalpha():
            modifiedText+=char.upper()
    return modifiedText

def getKeyL_shift(ciphertext):
    # your code here
    ciphertext = remove_nonalpha(ciphertext)
    counts = [0] * 21
    for i in range(1,21):
        s = shift_string(ciphertext, i, 'r')
        matches = 0
        for j in range(i, len(s)):
            if ciphertext[j] == s[j]:
                matches += 1
                counts[i] = matches
    maxN = counts[0]
    for num in counts:
        if num > maxN:
            maxN = num
    k = counts.index(maxN)
    return k

def shift_string(s,n,d):
    if d != 'r' and d!= 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n%len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

def get_cipherType(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not ciphertext.strip():
        return "Empty Ciphertext"
    cipherType = ""
    only_text = remove_nonalpha(ciphertext)
    if (only_text == ""):
        cipherType = "Polybius Square Cipher"
        return cipherType
    chiSquared = (get_chiSquared(ciphertext))
    if(chiSquared < 400):
        cipherType = "Spartan Scytale Cipher"
        return cipherType
    else: 
        i = (get_indexOfCoin(ciphertext))
        if (i > 0.062 and i < 0.068):
            flipped_cipher = ""
            for c in only_text:
                flipped_cipher += alphabet[25 - alphabet.index(c)]
            flipped_Chi = get_chiSquared(flipped_cipher)
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
def freq_analysis(message):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    count_list = []
    i = 0
    while i < 52:
        count_list.append(0)
        i += 1
    array = []
    for i in message:
        array.append(i)
    n = len(array) + 0.0
    # counts occurences of each letter
    for x in array:
        i = 0
        while i < 52:
            if x == alphabet[i]:
                count_list[i] += 1
            i += 1
    tupleList = []

    
    freq_list = []
    for x in count_list:
        freq_list.append(x/n)

    for x in range(52):
        tupleList.append(tuple((alphabet[x],freq_list[x])))
    sortedStuff = sorted(tupleList, key=lambda tup:tup[1],reverse=True)
    print()
    print(sortedStuff)
    print()

    #i = 0
    #while i < 52:
    #    print(str(alphabet[i]) + ": " + str(freq_list[i]))
    #    i+=1
    return freq_list


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

def getKeyL_friedman(ciphertext):
    # your code here
    n = len(ciphertext)
    I = get_indexOfCoin(ciphertext)
    k = math.ceil((0.027 * n)/((n-1)*I+0.065-0.038*n))
    return k

def test_cipher(ciphertext):
    ciphertext_stripped = remove_nonalpha(ciphertext)
    keyL_shift = getKeyL_shift(ciphertext_stripped)
    keyL_friedman = getKeyL_friedman(ciphertext)
    I = get_indexOfCoin(ciphertext)
    chi = get_chiSquared(ciphertext)
    print("Shift Test Key Length: " + str(keyL_shift))
    print("Friedman Test (key length): " + str(keyL_friedman))
    print("Index of Coincidence: " + str(I))
    print("Chi-value: " + str(chi))
    print()
    print("Frequency Analysis:----------------")
    freq = freq_analysis(ciphertext)
    print("-----------------------------------")
    cipherType = get_cipherType(ciphertext)
    print("CipherType test: " + cipherType)
    

def cryptanalysis_shift(ciphertext):
    chiList = [round(get_chiSquared(d_shift(ciphertext,(i,'l'))),4) for i in range(26)]
    key = chiList.index(min(chiList))
    key = (key,'l')
    plaintext = d_shift(ciphertext,key)
    return key,plaintext

#-----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName,'r')
    contents = inFile.read()
    inFile.close()
    return contents

#-----------------------------------------------------------
# Parameters:   text (string)
#               filename (string)            
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
#-----------------------------------------------------------
def text_to_file(text, filename):
    outFile = open(filename,'w')
    outFile.write(text)
    outFile.close()
    return

#-----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#-----------------------------------------------------------
# Parameters:   None 
# Return:       squqre (list of strings)
# Description:  Constructs Vigenere square as list of strings
#               element 1 = "abcde...xyz"
#               element 2 = "bcde...xyza" (1 shift to left)
#-----------------------------------------------------------
def get_vigenereSquare():
    alphabet = get_lower()
    return [shift_string(alphabet,i,'l') for i in range(26)]

#-----------------------------------------------------------
# Parameters:   None 
# Return:       list 
# Description:  Return a list with English language letter frequencies
#               first element is frequency of 'a'
#-----------------------------------------------------------
def get_freqTable():
    freqTable = [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
                 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    return freqTable

#-----------------------------------------------------------
# Parameters:   text (str) 
# Return:       list: wordCount 
# Description:  Count frequency of letters in a given text
#               Returns a list, first element is count of 'a'
#               Counts both 'a' and 'A' as one character
#-----------------------------------------------------------
def get_charCount(text):
    return [text.count(chr(97+i))+text.count(chr(65+i)) for i in range(26)]

#-------------------------------------------------------------------
# Parameters:   s (string): input string
#               n (int): number of shifts
#               d (str): direction ('l' or 'r')
# Return:       s (after applying shift
# Description:  Shift a given string by n shifts (circular shift)
#               as specified by direction, l = left, r= right
#               if n is negative, multiply by 1 and change direction
#-------------------------------------------------------------------
def shift_string(s,n,d):
    if d != 'r' and d!= 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n%len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

#-----------------------------------------------------------
# Parameters:   text (string)
# Return:       double
# Description:  Calculates the Chi-squared statistics
#               chiSquared = for i=0(a) to i=25(z):
#                               sum( Ci - Ei)^2 / Ei
#               Ci is count of character i in text
#               Ei is expected count of character i in English text
#               Note: Chi-Squared statistics uses counts not frequencies
#-----------------------------------------------------------
def get_chiSquared(text):
    freqTable = get_freqTable()
    charCount = get_charCount(text)

    result = 0
    for i in range(26):
        Ci = charCount[i]
        Ei = freqTable[i]*len(text)
        result += ((Ci-Ei)**2)/Ei
    return result

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
#-----------------------------------------------------------
def load_dictionary(dictFile):
    inFile = open(dictFile, 'r',encoding=" ISO-8859-15") 
    dictList = inFile.readlines()
    i = 0
    for word in dictList:
        dictList[i] = word.strip('\n')
        i+=1
    inFile.close()
    return dictList

def load_dictionary_modified(dictFile,k):
    inFile = open(dictFile, 'r',encoding=" ISO-8859-15") 
    dictList = inFile.readlines()
    k = k+1
    i = 0
    newlist = []
    for word in dictList:
        temp = word.strip('\n')
        if (len(word) == k):
            newlist.append(temp)
            #print(dictList[i])
        i+=1
    inFile.close()
    return newlist

#-------------------------------------------------------------------
# Parameters:   text (string)
# Return:       list of words (list)
# Description:  Reads a given text
#               Each word is saved as an element in a list. 
#               Returns a list of strings, each pertaining to a word in file
#               Gets rid of all punctuation at the start and at the end 
#-------------------------------------------------------------------
def text_to_words(text):
    wordList = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i] != '':
                line[i] = line[i].strip(string.punctuation)
                wordList+=[line[i]]
    return wordList

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------
def analyze_text(text, dictFile):
    dictList = load_dictionary(dictFile)
    wordList = text_to_words(text)
    matches = 0
    mismatches = 0
    for word in wordList:
        #print(str(word) + "MATCH!")
        if word.lower() in dictList:
            matches+=1
        else:
            mismatches+=1
    return(matches,mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------
def is_plaintext(text, dictFile, threshold):
    if text == '':
        return False
    result = analyze_text(text, dictFile)
    percentage = result[0]/(result[0]+result[1])
    #print("Percentage: " + str(percentage))
    if threshold < 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: (shifts,direction) (int,str)
# Return:       ciphertext (string)
# Description:  Encryption using Shfit Cipher (Monoalphabetic Substitituion)
#               The alphabet is shfited as many as "shifts" using given direction
#               Non alpha characters --> no substitution
#               Valid direction = 'l' or 'r'
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_shift(plaintext, key):
    alphabet = get_lower()

    shifts, direction = key
    if shifts < 0:
        shifts*=-1
        direction = 'l' if key[1] == 'r' else 'r'
    shifts = key[0]%26
    shifts = shifts if key[1] == 'l' else 26-shifts
    
    ciphertext = '' 
    for char in plaintext:                          
        if char.lower() in alphabet:
            plainIndx = alphabet.index(char.lower())    
            cipherIndx = (plainIndx + shifts)%26        
            cipherChar = alphabet[cipherIndx]
            ciphertext+= cipherChar.upper() if char.isupper() else cipherChar 
        else:
            ciphertext+= char
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key: (shifts,direction) (int,str)
# Return:       ciphertext (string)
# Description:  Decryption using Shfit Cipher (Monoalphabetic Substitituion)
#               The alphabet is shfited as many as "shifts" using given direction
#               Non alpha characters --> no substitution
#               Valid direction = 'l' or 'r'
#               Algorithm preserves case of the characters
#               Trick: Encrypt using same #shifts but the other direction
#---------------------------------------------------------------------------------------
def d_shift(ciphertext, key):
    direction = 'l' if key[1]== 'r' else 'r'
    return e_shift(ciphertext,(key[0],direction))

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key,plaintext
# Description:  Cryptanalysis of shift cipher
#               Uses Chi-Square
#               Returns key and plaintext if successful
#               If cryptanalysis fails: returns '',''
#---------------------------------------------------------------------------------------
def cryptanalysis_shift(ciphertext):
    chiList = [round(get_chiSquared(d_shift(ciphertext,(i,'l'))),4) for i in range(26)]
    key = chiList.index(min(chiList))
    key = (key,'l')
    plaintext = d_shift(ciphertext,key)
    return key,plaintext

#-----------------------------------------------------------
# Parameters:   None 
# Return:       square (2D List)
# Description:  Constructs Playfair Square as lower case
#               alphabets placed in spiral fashion
#               Each element is a character
#               Square size is 5x5
#               The square does not have the character 'w'
#-----------------------------------------------------------
def get_playfairSquare():
    square = [['I', 'H', 'G', 'F', 'E'],
              ['J', 'U', 'T', 'S', 'D'],
              ['K', 'V', 'Z', 'R', 'C'],
              ['L', 'X', 'Y', 'Q', 'B'],
              ['M', 'N', 'O', 'P', 'A']]
    return square


#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (str,int,double)
# Return:       empty matrix (2D List)
# Description:  Create an empty matrix of size r x c
#               All elements initialized to pad
#               Default row and column size is 2
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[pad] * c for i in range(r)]

#-----------------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
#               Assumes given parameter is a valid matrix
#-----------------------------------------------------------
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return
#-----------------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
#-----------------------------------------------------------
def matrix_to_string(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=matrix[i][j]
    return text


def debug():
    baseString = get_baseString()
    baseString = adjust_key(baseString)
    ciphertext = file_to_text('ciphertext_Lucas_Krete_q3.txt')
    debug_substitution(ciphertext,baseString)
#-------------------------------------------------------------------------------------
# Parameters:   ciphertext (str)
#               baseString (str)
# Return:       None
# Description:  A debugging tool for substitution cipher
#---------------------------------------------------------------------------------------
def debug_substitution(ciphertext,baseString):
    subString = ['-' for i in range(len(baseString))]
    plaintext = ['-' for i in range(len(ciphertext))]
    print('Ciphertext:')
    print(ciphertext[:200])
    print()
    command = input('Debug Mode: Enter Command: ')
    description = input('Description: ')
    print()
    
    while command != 'end':
        subChar = command[8].lower()
        baseChar  = command[15].lower()

        if subChar == '#':
            subChar = '\n'
        if baseChar == '#':
            baseChar = '\n'
            
        if baseChar in baseString:
            indx = baseString.index(baseChar)
            subString[indx] = subChar
        else:
            print('(Error): Base Character does not exist!\n')

           
        print('Base:',end='')
        for i in range(len(baseString)):
            if baseString[i] == '\n':
                print('# ',end='')
            else:
                print('{} '.format(baseString[i]),end='')
        print()
        print('Sub :',end='')
        for i in range(len(subString)):
            if subString[i] == '\n':
                print('# ',end='')
            else:
                print('{} '.format(subString[i]),end='')
        print('\n')

        print('ciphertext:')
        print(ciphertext[:500]) # <---- you can edit this if you need to show more text
        for i in range(len(plaintext)):
            if ciphertext[i].lower() == subChar:
                if subChar == '#' or subChar == '\n':
                    plaintext[i] == '\n'
                else:
                    plaintext[i] = baseChar
        print('plaintext :')
        print("".join(plaintext[:500])) # <---- you can edit this if you need to show more text
        print('\n_______________________________________\n')
        command = input('Enter Command: ')
        description = input('Description: ')
        print()
    return
