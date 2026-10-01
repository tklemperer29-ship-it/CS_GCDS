"""
Program: Whats in a name
Author: Thea Klemperer
Bugs: only works for someone who has 3 names 
"""

# make a menu
import random 
name = input("What is your name? (only works for 3 names):")

def reverse_display(name):
    """
    Description: Takes a full name and returns the name in reverse order.
    Parameters: name (str) - the full name to be reversed.
    Returns: the parts of the name in reverse order
    """
    name_list = name.split(" ")
    reversed_name = name_list[2], name_list[1], name_list[0]
    print(reversed_name)
    return(reversed_name)
    



def count_vowels(name):
    """
    Description:  Counts the total number of vowels (a, e, i, o, u) in a name, including both uppercase and lowercase vowels.
    Parameters: Name (str) - the name that will be checked for vowels.
    Returns:int - the total number of vowels in the name.
    """
    #what does it do ?It counts the vowels in a name and it counts how many of each vowel 
    #variables that contain the running count of how many of each vowel in in the name that was inputed
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    #if done find a way to count y as vowel 
    vowel_count = 0
    index = 0 
    name = convert_to_lowercase(name)              #converts name to lowercase so it can be checked for vowels             
    while index < len(name):
        letter = name[index]
        if letter == "a":              #if letter is a, gets added to a count variable and add one to index so it moves onto next letter 
            a_count = a_count + 1
            index = index + 1
        elif letter == "e" :              #if letter is e, gets added to e count variable and add one to index so it moves onto next letter 
            e_count = e_count + 1
            index = index + 1
        elif letter == "i"  :             #if letter is i, gets added to i count variable and add one to index so it moves onto next letter 
            i_count = i_count + 1
            index = index + 1
        elif letter == "o" :              #if letter is o, gets added to o count variable and add one to index so it moves onto next letter 
            o_count = o_count + 1
            index = index + 1
        elif letter == "u" :              #if letter is u, gets added to u count variable and add one to index so it moves onto next letter 
            u_count = u_count + 1
            index = index + 1
        else:                                           # if the letter is not one of these vowels, just add one to index so it moves onto next letter 
            index = index + 1
        vowel_count = a_count + e_count + i_count + o_count + u_count       #vowel count is the sum of all of the vowels 
    print(vowel_count)
    specific_vowel = input("would you like the cound of a speific vowel (enter yes or no)")

    if specific_vowel == "yes":
        which_vowel = input("which vowel would you like to know the count of?")
        if which_vowel== "a":
            print(a_count)
        elif which_vowel == "e" :
            print(e_count)
        elif which_vowel == "i" :
            print(i_count)
        elif which_vowel == "o" :
            print(o_count)
        elif which_vowel == "u" :
            print(u_count)
    else:
        return(vowel_count)


def random_name(name):
    """
    Description:Takes a name, removes the spaces, and randomly scrambles all of the letters to create a new mixed-up name.
    Parameters: name (str) - the name whose letters will be randomly scrambled.
    Returns: str - the scrambled version of the name without spaces.

    """
    scrambled_name = ""                                     #variable to contain mixed up name 
    w_o_spaces = ""                                         # variable to contain the name withou spaces 
    split_name = name.split(" ")                            #varable to contain a list of each part of name being a different item in list 
    for human_name in split_name:
        w_o_spaces = w_o_spaces + human_name                #added each part of name to variable name without spaces so its all one big chunk with no spaces 
    
    while len(w_o_spaces) > 0:                              #while there are more than 0 characters in variable without spaces 
        random_index = random.randint(0, len(w_o_spaces) - 1)           #variable to find a random # between 0 and the length variable without spaces - 1
        scrambled_name = scrambled_name + w_o_spaces[random_index]      #add the letter whose index was the "random index" integer 
        w_o_spaces = w_o_spaces[:random_index] + w_o_spaces[random_index + 1:]      #

    print(scrambled_name)
    return(scrambled_name)
    


def return_first_name(name):    
    """
    Description: Takes a full name and returns only the first name.
    Parameters: name (str) - the full name that will be separated into parts.
    Returns: str - the first name.
    """    
    name_list = name.split(" ")
    print(name_list[0])
    return(name_list[0])



def return_middle_name(name):
    """
Description: Takes a full name and returns only the middle name.
Parameters: name (str) - the full name that will be separated into parts.
Returns: str - the middle name.
"""
    name_list = name.split(" ")
    if len(name_list) > 2:
        print(name_list[1])
        return(name_list[1])
    else:
        length = len(name_list) - 2
        return(name_list[length])



def return_last_name(name):
    """
    Description: Takes a full name and returns only the last name.
    Parameters: name (str) - the full name that will be separated into parts.
    Returns: str - the last name.
    """
    name_list = name.split(" ")
    length = len(name_list) - 1
    print(name_list[length])
    return(name_list[length])



def hyphen_in_lastname(name):
    """
    Description: Checks if a name contains a hyphen and returns True if it does and False if it does not.
    Parameters: name (str) - the name that will be checked for a hyphen.
    Returns: Returns boolean - true if name contains hyphen, false if anything else
    """
    "-" == True
    name_letters = list(name)
    if "-" in name_letters:
        print("contains hyphen")
        return True
    else:
        print("no hyphen")
        return False
        


def convert_to_lowercase(name):
    """
    Description: Converts all uppercase letters to lowercase  
    Parameters:name (str) - the name that will be converted to lowercase.
    Returns: str - the name with all uppercase letters converted to lowercase. 
    """
    output = ""                                                         #stores the converted name
    letters = list(name)                                                #separates the name into individual characters
    for letter in letters:
        num = ord(letter)                                               # finds the ASCII value of each character
        if num >= 97 and num <= 122:                                    #ASCII values for lowercase letters are between 97 and 122
            output= output+letter 
        elif num >= 65 and num <= 90:                                   #ASCII values for uppercase letters are between 65 and 90
            num = num + 32                                              # Adds 32 because lowercase ASCII values are 32 greater than uppercase values
        else: 
            output = output + letter 
    return output

def convert_to_uppercase(name):
        
    """
    Description: Converts all lowecase letters to uppercase  
    Parameters:name (str) - the name that will be converted to uppercase.
    Returns: str - the name with all lowercase letters converted to uppercase. 
    """
    output = ""                                                         #stores the converted name
    letters = list(name)                                                #separates the name into individual characters

    for letter in letters:
        num = ord(letter)                                               # finds the ASCII value of each character

        if num >= 97 and num <= 122:                                    #ASCII values for lowercase letters are between 97 and 122
            num = num - 32                                                  #subtracts 32 because lowercase ASCII values are 32 greater than their uppercase equivalents
            output = output + chr(num)

        elif num >= 65 and num <= 90:                                    #ASCII values for uppercase letters are between 65 and 90 
            output = output + letter

        else:
            output = output + letter

    return output




def menu(convert_to_lowercase,hyphen_in_lastname, return_last_name, return_middle_name, return_first_name, random_name, count_vowels, reverse_display,convert_to_uppercase): 
    """
    Description: Displays a menu of options for the user to choose from and calls the corresponding function based on the user's input.
    Parameters: convert_to_lowercase, hyphen_in_lastname, return_last_name, return
_middle_name, return_first_name, random_name, count_vowels, reverse_display, convert_to_uppercase - functions that will be called based on user input.
    Returns: None
    """

    while True:
        call_func = input("Please type the number of the option you would like to choose:\n"
 "1. Reverse the order of your name.\n"
 "2. Count the vowels in your name.\n"
 "3. Scramble the letters in your name.\n"
 "4. Show your first name.\n"
 "5. Show your middle name.\n"
 "6. Show your last name.\n"
 "7. Check if your name contains a hyphen.\n"
 "8. Convert your name to lowercase.\n"
 "9. Convert your name to uppercase.\n"
 "Enter your choice: ")
        if call_func == "1":
            reverse_display(name)
        elif call_func == "2":
            count_vowels(name)
        elif call_func == "3":
            random_name(name)
        elif call_func == "4":
            return_first_name(name)
        elif call_func == "5":
            return_middle_name(name)
        elif call_func == "6":
            return_last_name(name)
        elif call_func == "7":
            hyphen_in_lastname(name)
        elif call_func == "8":
            convert_to_lowercase(name)
            print("Your name in lowercase is: " + convert_to_lowercase(name))
        elif call_func == "9":
            convert_to_uppercase(name)
            print("Your name in uppercase is: " + convert_to_uppercase(name))
        else:
            print("Please enter valid response")
        

menu(convert_to_uppercase, convert_to_lowercase,hyphen_in_lastname, return_last_name, return_middle_name, return_first_name, random_name, count_vowels, reverse_display )




 