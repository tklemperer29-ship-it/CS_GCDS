color = "pink"

while True :
    guess = input ('enter your color guess :').lower()

    if color == guess :
        print ("You_got_it")
        break
    else :
        print ("try_again")