"""
Program: Words after "G"/"g"

-split the words by building a placeholder variable: word
    -loop each character in the input string
    -check if character is a letter
    -add a letter to word each loop until a non-alpha char is encountered
-if character is alpha
    -add character to word
    -non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
-else
    -check if word is greater than "g" alphabetically
        -print word
        -set word = empty string
    -or else
        -set word = empty string and build the next word
"""
def words():
    quote = input("Enter a 1 sentence quote, non-alpha separate words: ")
    word = ""
    for ltr in quote:
        if ltr.isalpha():
            word = word + ltr
        else:
            if word[0].lower() > "g":
                print (word.upper())
                word = ""
            else: 
                word = ""
words()
