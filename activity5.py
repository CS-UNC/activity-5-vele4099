

def more_than_20(file):
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