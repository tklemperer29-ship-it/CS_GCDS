# make a menu
import random 
name = input("What is your name?")

def reverse_display(name):
    #What does it do? it takes names and rverses them ex: Thea Sirota to Sirota Thea
    name_list = name.split(" ")
    reversed_name = name_list[2], name_list[1], name_list[0]
    print(reversed_name)

reverse_display(name)

def count_vowels(name):
    #what does it do ?It counts the vowels in a name and it counts how many of each vowel 
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    #if done find a way to count y as vowel 
    vowel_count = 0
    index = 0 
    while index < len(name):
        letter = name[index]
        for letter in name:
            if letter == "a" or letter == "A": 
                a_count = a_count + 1
                index = index + 1
            if letter == "e" or letter == "E":
                e_count = e_count + 1
                index = index + 1
            if letter == "i"  or letter == "I":
                i_count = i_count + 1
                index = index + 1
            if letter == "o" or letter == "O":
                o_count = o_count + 1
                index = index + 1
            if letter == "u" or letter == "U":
                u_count = u_count + 1
                index = index + 1
            else:
                index = index + 1
            vowel_count = a_count + e_count + i_count + o_count + u_count
    print(vowel_count)
count_vowels(name)

def random_name(name):
    #function mixes up name to create new name 
    newfullname = ""
    output = ""
    name_list = name.split(" ")
    for human_name in name_list:
        og_name_letters = list(human_name)

        output = random.shuffle(og_name_letters)
        print(output)
        #newfullname.append(name_letters)
    

    print(newfullname)



random_name(name)

    
    




# if extra time def hang_man(): 
