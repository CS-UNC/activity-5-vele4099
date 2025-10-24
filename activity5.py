

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

'''
3x Uses_Only function:
uses_only("cat", "at") 
    ^returns [False] as cat uses 'c' and that letter does not appear in "at"
uses_only("cat", "tac")
    ^returns [True] as "CAT" uses 't' 'a' 'c'
uses_only("ct", "cat)
    ^returns True as cat uses 'c' and 't' exist in "cat"
'''

def uses_only(word, letters):
    #Each character from words needs to appear in Letters,
    for let in word:
        #for each char in word, check if its in
        if let not in letters:
            #Letter Exist, but not in "letters" [break-loop]
            return False
    return True

def all_uses_only(file, letters):
    valid_words = []
    words_file = open(file, 'r')

    for line in words_file:
        ## Copy Previous Code to Open File (returns single word string no spaces)
        word = line.strip()
        # Check each word with uses_only; add valid ones to the list
        if uses_only(word, letters):
            valid_words.append(word)
        #return our list
    return (valid_words)

done = all_uses_only("CROSSWD.txt", "ag")

print(done)