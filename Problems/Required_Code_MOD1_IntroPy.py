def words():
    quote = input("Enter a 1 sentence quote, non-alpha separate words: ")
    word = ""
    for ltr in quote:
        if ltr.isalpha():
            word = word + ltr
            #need to finish
            #incomplete
