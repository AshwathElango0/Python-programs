from random import choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_on='y'
while game_on=='y':
        
    dealer_hand=[]
    dealer_hand.append(choice(cards))
    print("Dealer's hand", dealer_hand)
    dealer_hand.append(choice(cards))
    dsum=0
    for i in dealer_hand:
        dsum+=i


    your_hand=[]
    your_hand.append(choice(cards))
    your_hand.append(choice(cards))    
    print("Your hand", your_hand)
    askplayer=input("Do you wish to draw a card?")
    if askplayer=='y':
        your_hand.append(choice(cards))
    usum=0
    for i in your_hand:
        usum+=i
        
    if dsum<17:
        dealer_hand.append(choice(cards))
        dsum=0
        for i in dealer_hand:
            dsum+=i
            
    if usum>21:
        print(your_hand)
        print("You lose")
    elif dsum>21:
        print("Dealer's hand", dealer_hand)
        print("Your hand", your_hand)
        print("WIN")
        
    else:
        if usum == dsum:
            print("Dealer's hand", dealer_hand)
            print("Your hand", your_hand)
            print("Draw")
            
        elif usum>dsum:
            print("Dealer's hand", dealer_hand)
            print("Your hand", your_hand)
            print("WIN")
            
        else:
            print("Dealer's hand", dealer_hand)
            print("Your hand", your_hand)
            print("L bazo")
            
    
        
        

    
    

    
        
    game_on=input("Want a rematch?")
        