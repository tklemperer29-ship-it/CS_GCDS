print("""                                                                                               #Blurb explaining my algorithm 
Blackjack Hit Analyzer and Card Counting Tool
---------------------------------------------

This program simulates a blackjack hand and calculates key metrics to guide player decisions.

Main features:
1. Calculates your current hand total, including correct handling of aces (soft/hard).
2. Determines the probability of busting or hitting 21 if you take a hit.
3. Tracks all cards seen and updates a running count for card counting.
4. Computes the true count (running count adjusted for how many cards are left in the deck) to estimate player advantage.
5. Allows multiple hits, updating probabilities and hand totals dynamically.

How the metrics can be used:
- Bust probability: Helps players decide whether hitting is safe.
- Chance to hit 21: Shows the likelihood of reaching 21 on the next card.
- True count: Used in card counting strategies. Positive true count favors the player (more high cards left), negative favors the dealer.
- The higher or lower the true count is, the more the player or dealer is advantaged.
       
This tool is educational and intended to teach blackjack strategy, probability, and card counting.
      
-------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------- LETS PLAY ----------------------------------------------------------------
                                                                ┌─────┐
                                                                │A    │
                                                                │  ♠  │
                                                                │    A│────┐
                                                                └─────┘    │
                                                                    │  ♠   │
                                                                    │     K│
                                                                    └───── ┘
-------------------------------------------------------------------------------------------------------------------------------------------

""")

def apply_hit(hand_total, soft_aces, card, values):                                                     #A funcion that defines a reuseable subprogram that i will reference later
    if card == "ace":                                                                                       # If the card is an ace
        if hand_total + 11 <= 21:                                                                               #and if the hand total + 11 is less than or equal to 21
            hand_total += 11                                                                                        # then add 11 to the hand total 
            soft_aces += 1                                                                                          # and add 1 to the soft aces 
        else:                                                                                                   # or else:
            hand_total += 1                                                                                         # add one to the hand total 
    else:                                                                                                    # if the card is not an ace:
        hand_total += values[card]                                                                                  # hand total becomes the added values of the cards found in the list "values" 

    if hand_total > 21 and soft_aces > 0:                                           #condition based on if the hand total is greater than 21 and the soft aces are above 0:
        hand_total -= 10                                                            # then subtract 10 from the hand total 
        soft_aces -= 1                                                              # and subtract 1 from the soft aces 

    return hand_total, soft_aces                                                    #updates variables 

running_count = 0                                                                   # variable running count = 0 

deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","jack","jack",
        "jack","jack","queen","queen","queen","queen","king","king","king","king","ace","ace", "ace","ace"]  #the variable "deck = this list "
values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"jack":10,"queen":10,"king":10} # creates a dictionary 

while True:
    shuffled = input("Was the deck shuffled or is it the start of the program? (answer yes or no) ")                                                  #ask if deck was shuffled
    
    if shuffled.lower() in ["yes", "ye", "y","yea"]:                                                                            # if the answer is one of the things in the list enter loop 
        running_count = 0                                                                           #redefine running count as 0 
        decks_remaining = int(input("How many decks are in the sleeve? (answer with an integer)"))                         #ask and replace how many decks there are (used for truecount and total cards for bust probibility)
        total_cards = decks_remaining * deck                                                        #the total amount of cards that are being played with is the # of decks x the 52 cards in the deck 
    
    dealers_hand = input("What's the dealer showing? Include only values, exclude suits, and separate by spaces. If the value is an integer, write it as an integer: ").lower().split()  #ask and replace for how many cards the dealer has, used for card count and if i get to it dealer bust probibility 
    your_hand = input("What are your cards? Include only values, exclude suits, and separate by spaces. If the value is an integer, write it as an integer:").lower().split()           #aks and replace for what your cards are, used for card count and to calculate your bust probibility 
    others_hand = input("What cards do the other people at the table have? Include only values, exclude suits, and separate by spaces. If the value is an integer, write it as an integer:").lower().split()  #ask a replace what other people at the table have, used for card count and helps and goes toward bust probibilty 

    hand_total = 0                                                      #A variable for what the cards in your hand add up to     
    soft_aces = 0                                                       # a variable to count aces that currently equals 0 

    for card in your_hand:                                              #go through the cards in variable your_hand one by one
        if card == "ace":                                                # if the crard is an ace:
            soft_aces += 1                                              # add one to the soft aces
        else:                                                           # or else:
            hand_total += values[card]                                      #add this card to the running total of this hand 
    for i in range(soft_aces):                                          #repeat for each ace
        if hand_total + 11 <= 21:                                       #if hand total + 11 is less than or equal to 21:
            hand_total += 11                                            #add 11 to hand total 
        else:                                                           # or else:
            hand_total += 1                                             #add one to hand total 
            soft_aces -=1                                               #subtract one to soft aces 
    busts = 0                                                       #variable to keep track of how many scenarioes end in bust 
    blackjacks = 0                                                  #variable to keep track of how many scenarioes end in blackjack
    total = len(total_cards)                                                        #variable total defined as # of things in list total cards 
    new_total = hand_total                                                             #variable new total = hand total 

    for card in total_cards:                                                        #go through every card in total cards
        hit_total, hit_soft_aces = apply_hit(hand_total, soft_aces, card, values)   #fake hitting without actually changing the actual hand

        if hit_total > 21:                                                          #If the hit total is greater than 21
            busts += 1                                                              #Add one to variable busts 
        elif hit_total == 21:                                                       #else if hit total equals 21:
            blackjacks += 1                                                         #add 1 to the variable blackjacks 

    
    bust_prob = (busts / total) * 100                                               #variable bust prob is the ammount of scenarios that result in a bust divided by the total number of scenarios then multiplied by 100 
    blackjack_prob = (blackjacks / total) * 100                                     #variable blackjack prob is the ammount of scarios that result in the hand total equaling 21 divided by the total number of scernaios  then multiplied by 100 
    
    print(" ---- Hit Analysis ---- ")                                               #Disply hit analysis, visually pleasing 
    print(f"Your current hand total is {hand_total}")                               #Display hand total 
    print(f"If you hit, you are {bust_prob:.1f}% likely to bust")                       #Displays message "If you hit, you are {bust_prob}% likely to bust" with the bust prob inserted 
    print(f"if you hit, you are {blackjack_prob:.1f}% likely to get 21")         #Display message "if you hit, you are {blackjack_prob}% likely to get 21") with prob of 21 inserted 
    print("" \
    "" \
    "")

    hit_cards_all = []

    hit_again = input("Did you hit again? ").lower()
    
    while hit_again in ["yes", "y", "ye", "yea"]:
        hit_cards = input("What card did you receive? ").lower().split()                   #new variable for the card recieved upon hitting 
        hit_cards_all.extend(hit_cards)
        
        for card in hit_cards:
            if card in total_cards:
                total_cards.remove(card)
            hand_total, soft_aces = apply_hit(hand_total, soft_aces, card, values)
    
        if hand_total > 21:                                                     #If hand total is over 21 
            print("You busted")                                                #display "you busted"
            break                                                               #quit loop 

        n_busts = 0                                                             #another variable for bust for a different context than before 
        n_blackjacks = 0                                                        #another variable for 21 for a diffenet context than before 
        new_total = len(total_cards)

        for card in total_cards:
            test_total, test_soft_aces = apply_hit(hand_total, soft_aces, card, values)
            
            if test_total > 21:
                n_busts += 1
            elif test_total == 21:
                n_blackjacks += 1

        second_bust_prob = (n_busts / new_total) * 100                                      #calculates probobility of busting 
        second_blackjack_prob = (n_blackjacks / new_total) * 100                            # calculates probobility of user getting 21
        print(f"Your current hand total is {hand_total}")
        print(f"If you hit again, you are {second_bust_prob:.2f}% likely to bust")              # tells user the probibility of them busting 
        print(f"If you hit again, you are {second_blackjack_prob:.2f}% likely to get 21")        #tells user the probobility of them getting 21 if they hit 
        print("" 
              
        "")
        hit_again = input("Did you hit again?").lower()                                             # asking user if they hit again 

    dealers_cards = input("What was the dealers hidden card and the cards they recived upon hitting (if the hit)?").lower().split()          #variable for the dealers hidden cards 
    cards_shown = dealers_hand + your_hand + others_hand + hit_cards_all + dealers_cards                                            #variable cards shown = all these lists

    for card in cards_shown:                                                             #go through every card in cards shown 
        if card in total_cards:                                                                 #if the card is in list total cards:
            total_cards.remove(card)                                                                    # remove the card from total cards 
        if card in ["2","3","4","5","6"]:                                                       # if the card is 2-6, add one to the running count 
            running_count += 1                                                                          #Add 1 to the running count 
        elif card in ["10", "jack", "queen", "king", "ace"]:                                    #or else if the card is 10, jack, queen, king, or ace, subtract 1 from the running count 
            running_count -= 1

    true_count = running_count/decks_remaining                                             #calculates true count by dividing running count by decks remaining 

    print(f"The truecount is {true_count:.2f}")                                                                       # display true count 
    
    if true_count > 0:                                                                                                  #on the condition that the true count is greater than 0:
        print("Advantage: PLAYER")                                                                                              #Display the message 
    elif true_count < 0:                                                                                                    #on the condition that the true count is less than 0 :
        print("Advantage: DEALER")                                                                                              #display this message 
    elif true_count == 0:                                                                                                        # on the condition that the true count = 0:
        print("Advantage: Neutral")                                                                                #display this message 

    print("-" * 40)                                                                                                                 #Display barrier 