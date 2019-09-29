#--------------------------
# Your Name and ID: Luke Krete 160758350
# CP460 (Fall 2019)
# Assignment 1
#--------------------------


import math
import string

#---------------------------------
#       Given Functions          #
#---------------------------------
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

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Scytale Cipher
#               Key is the diameter, i.e. # rows
#               Assume infinte length rod (infinte #columns)
#--------------------------------------------------------------
def e_scytale(plaintext, key):
    # By definition, number of rows is key
    r = int(key)
    # number of columns is the length of ciphertext/# rows    
    c = int(math.ceil(len(plaintext)/key))
    # create an empty matrix for ciphertext rxc
    cipherMatrix = new_matrix(r,c,"")

    # fill matrix horizontally with characers, pad empty slots with -1
    counter = 0
    for i in range(r):
        for j in range(c):
            cipherMatrix[i][j] = plaintext[counter] if counter < len(plaintext) else -1
            counter+=1

    #convert matrix into a string (vertically)
    ciphertext = ""
    for i in range(c):
        for j in range(r):
            if cipherMatrix[j][i]!=-1:
                ciphertext+=cipherMatrix[j][i]
    return ciphertext


#---------------------------------
#       Problem 1                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Scytale Cipher
#               Assumes key is a valid integer in string format             
#---------------------------------------------------
def d_scytale(ciphertext, key):
    plaintext = ''
    rows = key
    temp = 0
    new_ciphertext = ciphertext[::-1]
    columns = int(math.ceil(len(ciphertext)/rows))
    #print(new_ciphertext)
    cipherMatrix = new_matrix(rows,columns,"")
    if key <1:
        return plaintext
    #columns = int(math.ceil(len(ciphertext)/rows))
    check = (rows*columns)-len(ciphertext)
    if (check > columns):
        return plaintext
    else:
        if check >0:
            new_ciphertext = "^" + new_ciphertext
            check-=1
        while check > 0:
            temp = temp + key
            new_ciphertext = new_ciphertext[:temp] + "^" + new_ciphertext[temp:]
            check-=1
    new_ciphertext = new_ciphertext[::-1]
    #print(new_ciphertext)
    counter = 0
    for i in range(columns):
        for j in range(rows):
            cipherMatrix[j][i] = new_ciphertext[counter]
            counter+=1
    for i in range(rows):
        for j in range(columns):
            if cipherMatrix[i][j] != "^":
                plaintext+=cipherMatrix[i][j]
    #print(plaintext)
    return plaintext

#---------------------------------
#       Problem 2                #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
#-----------------------------------------------------------
def load_dictionary(dictFile):
    dictList = []
    with open(dictFile, 'r',encoding="mbcs") as f:
        for line in f:
            line = line.strip()
            dictList.append(line)
    # your code here
    return dictList

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
    data = text.strip().split()
    # your code here
    for word in data:
        #table = str.maketrans({key: None for key in string.punctuation})
        #new_word = word.translate(table)
        word = word.strip(string.punctuation)
        wordList.append(word)
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
    matches = 0
    mismatches = 0
    dictList = load_dictionary(dictFile)
    wordList = text_to_words(text)
    new_dictList = []
    for word in dictList:
        word = word.lower()
        new_dictList.append(word)
    for word in wordList:
        if word.lower() in new_dictList:
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
    if(threshold < 0 or threshold > 1):
        threshold = 0.9
    matches, mismatches = analyze_text(text,dictFile)
    if(matches >0 and mismatches >= 0):
        if ((matches/(matches + mismatches)) >= threshold):
            return True
    # your code here
    return False

#---------------------------------
#       Problem 3                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   cipherFile (string)
#               dictFile (string)
#               startKey (int)
#               endKey (int)
#               threshold (float)
# Return:       key (string)
# Description:  Apply brute-force to break scytale cipher
#               Valid key range: 2-100 (if invalid --> print error msg and return '')
#               Valid threshold: 0-1 (if invalid --> print error msg and return '')
#               If decryption is successful --> print plaintext and return key
#               If decrytpoin fails: print error msg and return ''
#---------------------------------------------------
def cryptanalysis_scytale(cipherFile, dictFile, startKey, endKey, threshold):
    text = file_to_text(cipherFile)
    if(startKey >=2 and endKey <=100):
        if(threshold >= 0 and threshold <=1):
            for testKey in range(startKey, endKey):
                test = d_scytale(text, testKey)
                #print(test)
                plaintextCheck = is_plaintext(test, dictFile, threshold)
                if(plaintextCheck == True):
                    print("Key found! " + str(testKey))
                    print(test)
                    return testKey
                else:
                    print("Key " + str(testKey) + " failed!")
                    
    return ''

#---------------------------------
#       Problem 4                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   None
# Return:       polybius_square (string)
# Description:  Returns the following polybius square
#               as a sequential string:
#               [1] [2]  [3] [4] [5] [6] [7] [8]
#           [1]      !    "   #   $   %   &   '
#           [2]  (   )    *   +   '   -   .   /
#           [3]  0   1    2   3   4   5   6   7
#           [4]  8   9    :   ;   <   =   >   ?
#           [5]  @   A    B   C   D   E   F   G
#           [6]  H   I    J   K   L   M   N   O
#           [7]  P   Q    R   S   T   U   V   W
#           [8]  X   Y    Z   [   \   ]   ^   _
#---------------------------------------------------
def get_polybius_square():
    polybius_square = ''
    for i in range(32,96):
        polybius_square = polybius_square + chr(i)
    return polybius_square

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (none)
# Return:       ciphertext (string)
# Description:  Encryption using Polybius Square
#--------------------------------------------------------------
def e_polybius(plaintext, key):
    ciphertext = ''
    polybius_string = get_polybius_square()
    for char in plaintext:
        if char != '\n':
            # finding row of the table 
            index = polybius_string.index(char.upper()) + 1
            x = math.ceil(index / 8)
            y= index - (8*(x-1))
            # finding column of the table            
            ciphertext = ciphertext + str(x)
            ciphertext = ciphertext + str(y)
        else:
            ciphertext = ciphertext + '\n' 
    # your code here
    return ciphertext

#---------------------------------
#       Problem 5                #
#---------------------------------

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (none)
# Return:       plaintext (string)
# Description:  Decryption using Polybius Square Cipher
#               Detects invalid ciphertext --> print error msg and return ''
#               Case 1: #of chars (other than \n) is not even
#               Case 2: the ciphertext contains non-numerical chars (except \n')
#-------------------------------------------------------
def d_polybius(ciphertext, key):
    plaintext = ''
    polybius_string = get_polybius_square()
    polybius_m = new_matrix(8,8,"")
    counter = 0
    p1 = ""
    p2 = ""
    for i in range (8):
    	for j in range(8):
    		polybius_m[i][j] = polybius_string[counter]
    		counter+=1
    #print_matrix(polybius_m)
    num_newlines = ciphertext.count('\n')
    if ((len(ciphertext) - num_newlines) % 2 > 0):
    	print("Invalid Ciphertext, decryption failed")
    	return ''
    for letter in ciphertext:
    	if letter.isalpha():
    		print("Invalid Ciphertext, decryption failed")
    		return ''
    index = 0
    while(index < len(ciphertext)):
    	p1 = ciphertext[index]
    	index = index + 1
    	if p1 != '\n':
    	    p2 = ciphertext[index]
    	    index += 1
    	    #print("P1: " + p1 + "  P2: " + p2)
    	    #print(plaintext)
    	    plaintext = plaintext + polybius_m[int(p1)-1][int(p2)-1]
    	else:
    	    plaintext = plaintext + '\n'
    # your code here
    return plaintext


















