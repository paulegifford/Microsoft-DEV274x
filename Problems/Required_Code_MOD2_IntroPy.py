"""
Program: list-o-matic

This program takes string input and checks if that string is in a list of strings
  -if string is in the list it removes the first instance from list
  -if string is not in the list the input gets appended to the list
  -if the string is empty then the last item is popped from the list
  -if the list becomes empty the program ends
  -if the user enters "quit" then the program ends

"""
alist = ["dog", "cat", "monkey", "rhino"]

def list_o_matic(alist, user_input):
    if user_input == "":
        print(alist.pop(), "popped from list")
    else:
        if user_input in list:
            print(user_input, "removed from the list")
            return alist.remove(user_input)
        else:
            print(user_input, "added to the list")
            return alist.append(user_input)
while alist:
    print("Look at all the animals:", alist)
    user_input = input("enter the name of an animal")
    if user_input == "Quit".lower():
        print("Goodbye")
    else:
        list_o_matic(alist, user_input)
