words_file = open('CROSSWD.txt','r')

'''prints each word
for i in words_file: 
    print(i)

    
'''
print([x for x in dir(words_file) if '_' != x[0]])



''' 
for i in words_file:
print(words_file.readline())
print(i.strip())  
'''


#Write a function twenty_or_more(string)
#indicating the path to the file to consider and returns all words read from the file that have more than 20 characters as a list. Note that you will have to open the file indicated in file for reading, and iterate over all lines in the file. Also remember that you can add values to a list using the .append(value) method
def more_than_20(file):
    long_words = []
    words_file = open(file, 'r')

    for line in words_file:
        ## Decode Each Line from input file + strip the special characters.
        word = line.strip()
        #Check Word Length
        if len(word) >= 20: 
            long_words.append(word)
    return(long_words)

results = more_than_20('CROSSWD.txt')

print(results)

def has_no_e(word):
    let = 'e'
    return(let not in word)

print(has_no_e("hello"))

def uses_only(word,letters):
    for let in letters:
        if let not in word:
            return False
    return True