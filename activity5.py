
#Write a function twenty_or_more(string)
#indicating the path to the file to consider and returns all words read from the file that have more than 20 characters as a list. Note that you will have to open the file indicated in file for reading, and iterate over all lines in the file. Also remember that you can add values to a list using the .append(value) method
def twenty_or_more(file):
    long_words = []
    words_file = open(file, 'r')

    for line in words_file:
        ## Decode Each Line from input file + strip the special characters.
        word = line.strip()
        #Check Word Length
        if len(word) > 20: 
            long_words.append(word)
    return(long_words)

def has_no_e(word):
    let = 'e'
    return(let not in word)

def uses_only(word,letters):
    for let in letters:
        #for each letter, check [if] inside string {word}
        if let not in word:
            return False
    return True