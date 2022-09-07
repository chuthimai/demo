import blackjack_art
import random as rd

print(blackjack_art.logo)

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8,
        9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    rd.shuffle(card)
    card_choice=card[0]
    card.pop(0)
    return card_choice

def put_one_card(cards):
    cards.insert(0,deal_card())
    return

def computer_put_one_card(computer_cards):
    while calculate_score(computer_cards)<18 and len(card)!=0:
        put_one_card(computer_cards)

def calculate_score(cards):
    if (11 in cards) and (sum(cards)>21):
        cards[cards.index(11)]=1
    sum_cards=sum(cards)
    return sum_cards

def compare(computer_score,user_score):
    if(user_score==computer_score or (user_score>21 and computer_score>21)):
        print("Draw 🙃🙃🙃.\n")
    elif(user_score>21 or computer_score==21):
        print("You lose 😤😤😤.\n")
    elif(computer_score>21 or user_score==21):
        print("You win 😎😎😎.\n")
    elif(computer_score>user_score):
        print("You lose 😭😭😭.\n")
    elif(computer_score<user_score):
        print("You win 😁😁😁.\n")
    return

is_game_over=False
is_game_start=True
user_cards = []
computer_cards = []

while is_game_over==False:
    if is_game_start==True:
        user_cards = []
        computer_cards = []
        put_one_card(user_cards)
        put_one_card(computer_cards)
        put_one_card(user_cards)
        put_one_card(computer_cards)
        is_game_start=False
    else:
        put_one_card(user_cards)
        print(f"The number of card left: {len(card)}")

    calculate_score(user_cards) # to print correct value of cards
    print(f"Computer's fist card: {computer_cards[0]}\nYour card: {user_cards}\nYour point is {calculate_score(user_cards)}")

    # user put one more card?
    if calculate_score(user_cards)<21:
        put_card = input("Do you want to put one more card? Yes or no? ").lower()

        if put_card == "yes" and calculate_score(user_cards) < 21 and len(card)!=0:
            continue

        elif put_card == "no" or calculate_score(user_cards) >= 21 or len(card)==0:

            # calculate and give result
            computer_put_one_card(computer_cards) #computer put some more
            calculate_score(computer_cards) # to print correct value of cards (when card is 11 or 1)
            print(f"Computer cards: {computer_cards}\nComputer point is {calculate_score(computer_cards)}")
            compare(calculate_score(computer_cards), calculate_score(user_cards))

            start = input("Do you want play continue? Yes or no? ").lower()
            if start == "yes":
                is_game_start = True
            else:
                is_game_over = True
    else:
        # calculate and give result
        computer_put_one_card(computer_cards) #computer put some more
        print(f"Computer cards: {computer_cards}\nComputer point is {calculate_score(computer_cards)}")
        compare(calculate_score(computer_cards), calculate_score(user_cards))

        start = input("Do you want play continue? Yes or no? ").lower()
        if start == "yes":
            is_game_start = True
        else:
            is_game_over = True




