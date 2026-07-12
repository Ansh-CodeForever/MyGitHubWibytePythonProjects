import csv
import random
import statistics as st

print('Wlcome to Top Trumps game - Skyscrapers and Dinosaurs edition!')
Top_Trumps = input('Please choose which edition you want to play with: \n1. Skyscrapers (S)\n2. Dinosaurs (D)\n')
rules = input('Do you want to read the rules of the game (Y/N)?')
if rules.lower() == 'y':
    print('1. Both players have 15 cards to start\n2. Choose a category from your card and compare it with the computer\'s card\n3. The player with the higher value in that category wins both cards\n4. If it is a draw, both cards are placed on the table for the next round\n5. The game continues until one player has all the cards')
else:
    print('Ok, let\'s start the game!')

#Training function
def training():
    display_best_card()
    print()
    Top_cards = input('Would you like to see the top N best cards for a category (Y/N)?')
    if Top_cards.lower() == 'y':
        try:
            n = int(input('How many best cards would you like to see (2-7)?'))
            if n < 2 or n > 7:
                print('Invalid number of cards, please enter a number between 2 and 7')
                n = int(input('How many best cards would you like to see (2-7)?'))
        except ValueError:
            print('Please enter a valid number between 2 and 7 (restart program)')
        for k in relevant_keys:
            print()
            print('Top ', n, 'best cards for ', k)
            display_top_best_cards(k, n)
            input()
    print()
    final_part = input('Would you like to do the final part of the training session (Y/N)?')
    print('Stats...')
    if final_part.lower() == 'y':
        print()
        min_max_ave()
    print('Training session is over, let\'s start the game!')

#Display the top N best cards for e
def display_top_best_cards(category, n):
    if Top_Trumps == 'S':
        if inv_mapping_dict[category] in ['H', 'F', 'B']:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]), reverse=True)
        else:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]))
    elif Top_Trumps == 'D':
        if inv_mapping_dict[category] in ['H', 'L', 'I', 'W']:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]), reverse=True)
        else:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]))
    #Length of all keys
    keys = list(all_cards_s[0].keys())
    keys_len = [len(key) for key in keys]

    longest_val = []
    for k in keys:
        all_cards_d = sorted(all_cards, key=lambda x: len(x[k]))
        longest_val.append(len(all_cards_d[-1][k]))

    max_col = zip(keys_len, longest_val)
    max_col = [max(m) for m in max_col]
    #Print keys and values
    for k in all_cards_s[0]:
        print(k, end = '')
        print((max_col[keys.index(k)] - len(k))*' ', end = '|')
    print()

    for card in all_cards_s[0:n:]:
        for k in card:
            print(card[k], end = '')
            print((max_col[keys.index(k)] - len(card[k]))*' ', end = '|')
        print()

#Display the best card for each category
def display_best_card():
    print('I will tell you the best card for each category.')
    print()
    for kk in relevant_keys:
        all_cards_s = sorted(all_cards, key=lambda x: float(x[kk]))
        if Top_Trumps == 'S':
            if inv_mapping_dict[kk] in ['H', 'F', 'B']:
                best_card = all_cards_s[-1]
            else:
                best_card = all_cards_s[0]
        else:
            if inv_mapping_dict[kk] in ['H', 'L', 'I', 'W']:
                best_card = all_cards_s[-1]
            else:
                best_card = all_cards_s[0]
        print('Best card for category', kk)
        display_card(best_card)
        input()
    print()

#Min/Max/Ave for all categories
def min_max_ave():
    for k in relevant_keys:
        metric = []
        metric = [float(card[k]) for card in all_cards]
        print('Max for', k, max(metric))
        print('Min for', k, min(metric))
        print('Average for', k, round(st.mean(metric), 2))
        print()

#Displaying the card function
def display_card(card):
    max_chars = 0
    for keys in card:
        if len(keys) > max_chars:
            max_chars = len(keys)

    for keys in card:
        print(keys, (max_chars - len(keys))*' ' , ': ', card[keys])

#determining the winner function
def determine_winner(m1, m2, order = 1):
    dict = {'player': m1, 'computer': m2}
    v = list(dict.values())
    k = list(dict.keys())

    if m1 == m2:
        return 'draw'
    else:
        if order == 1:
            return k[v.index(max(v))]
        else:
            return k[v.index(min(v))]
        
#Determining the rank of a card in a category, I made this function different from the class videos because in the class videos rank function I had lot of bugs
def category_rank(card, category):
    all_cards_s = sorted(all_cards, key=lambda x: float(x[category]))
    if Top_Trumps == 'S':
        if inv_mapping_dict[category] in ['H', 'F', 'B']:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]), reverse=True)
        else:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]))
    else:
        if inv_mapping_dict[category] in ['H', 'L', 'I', 'W']:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]), reverse=True)
        else:
            all_cards_s = sorted(all_cards, key=lambda x: float(x[category]))
    rank = all_cards_s.index(card) + 1
    return rank

#List of all the cards
if Top_Trumps == 'D':
    with open('Top Trumps - Dinosaurs.csv', mode = 'r') as file:
        csvFile = csv.DictReader(file)
        all_cards = list(csvFile)
elif Top_Trumps == 'S':
    with open('Top Trumps - Skyscrapers .csv', mode = 'r') as file:
        csvFile = csv.DictReader(file)
        all_cards = list(csvFile)
else:
    print('Did not understand your input, please enter S or D (retart program)')
    
#Distribution of cards to player and computer
relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]
random.shuffle(all_cards)

comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []
game_over = False

#Toss
mapping_dict = {}
inv_mapping_dict = {}

for key in relevant_keys:
    mapping_dict[key[0]] = key
    inv_mapping_dict[key] = key[0]

training_needed = input('Would you like a short training session (Y/N)?')
if training_needed.lower() == 'y':
    training()

print('Toss a coin to see who goes first...')
toss = input('Enter H for heads, T for tails: ')
toss_decider = random.choice(['H', 'T'])#I thought this was a more efficient way to do it than using random.randint(0, 1)
if toss == toss_decider:
    print('You won the toss, you go first!')
    chance = 'player'
else:
    print('Computer won the toss, computer goes first!')
    chance = 'computer'

#Main game loop
while not game_over:
    input('Press enter to continue...')
    print()

    player = player_cards.pop(0)
    comput = comput_cards.pop(0)
    table_cards.append(player)
    table_cards.append(comput)
    print('It is', chance, "'s turn to choose a category")

    print()
    print('Your card is...')
    display_card(player_cards[0])
    print()
    print('This card is...')
    if chance == 'player':
        print()
        try:
            chosen_key = input('What category is your choice?\n')
            chance = 'computer'
            key_requested = mapping_dict[chosen_key]
        except KeyError:
            print('Invalid key chosen, plaease enter a valid key')
            chosen_key = input('What category is your choice?\n')
            key_requested = mapping_dict[chosen_key]
        chance = 'computer'
    else:
        chosen_key = random.choice(list(mapping_dict.keys()))
        chance = 'player'
    key_requested = mapping_dict[chosen_key]
    value_player = player[key_requested]
    value_comput = comput[key_requested]

    print()
    print('Key of interest is...', key_requested)
    print()
    print('Player ', key_requested, 'is rank:', category_rank(player, key_requested))
    print('Computer ', key_requested, 'is rank:', category_rank(comput, key_requested))

    if Top_Trumps == 'S':
        if chosen_key in ['H', 'F', 'B']:
            winner = determine_winner(float(value_player), float(value_comput), 1)
        else:
            winner = determine_winner(float(value_player), float(value_comput), 0)
    else:
        if chosen_key in ['H', 'L', 'I', 'W']:
            winner = determine_winner(float(value_player), float(value_comput), 1)
        else:
            winner = determine_winner(float(value_player), float(value_comput), 0)

    print()
    print('Computer card is...')
    display_card(comput)
    print()
    print('Computer card is...')

    if winner == 'player':
        player_cards.extend(table_cards)
        table_cards.clear()
    elif winner == 'computer':
        comput_cards.extend(table_cards)
        table_cards.clear()

    print()
    if winner == 'draw':
        print('This round is a draw, cards are on the table for next round, no one looses cards')
    else:
        print(winner, 'wins this round!\nplayer has', len(player_cards), 'cards', 'computer has', len(comput_cards), 'cards')
    print('------------------------------------')
    
    if len(player_cards) == 0:
        print('Computer wins the game!')
        game_over = True
    elif len(comput_cards) == 0:
        print('Player wins the game!')
        game_over = True