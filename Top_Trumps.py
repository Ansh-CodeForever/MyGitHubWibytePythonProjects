import csv
import random

def display_card(card):
    max_chars = 0
    for keys in card:
        if len(keys) > max_chars:
            max_chars = len(keys)

    for keys in card:
        print(keys, (max_chars-len(keys))*' ', ': ', card[keys])

def determine_winner(m1, m2, order = 1):
    dict = {'player': m1, 'computer': m2}
    v = list(dict.values())
    k = list(dict.keys())

    if m1 == m2:
        return 'draw'
    else:
        if order == 1:
            return k[v.index(max(v))]

with open('Top Trumps - Skyscrapers.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)

relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]
random.shuffle(all_cards)

comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []
game_over = False
chance = 'player'

mapping_dict = {}

for key in relevant_keys:
    mapping_dict[key[0]] = key

while not game_over:
    player = player_cards.pop(0)
    comput = comput_cards.pop(0)
    table_cards.append(player)
    table_cards.append(comput)

    print()
    print('Player card is...')
    display_card(player_cards)
    if chance == 'player':
        print()
        chosen_key = input('What category is your choice?\n')
        chance = 'computer'
        key_requested = mapping_dict[chosen_key]
    else:
        key_requested = random.choice(relevant_keys)
        chance = 'player'

    value_player = float(player[key_requested])
    value_comput = float(comput[key_requested])

    print('Key of interest is...', key_requested)
    if chosen_key in ['H', 'F', 'Y']:
        winner = determine_winner(value_player, value_comput)
    else:
        winner = determine_winner(value_player, value_comput, 0)

    if winner == 'player':
        player_cards.extend(table_cards)
        table_cards.clear() 
    elif winner == 'computer':
        comput_cards.extend(table_cards)
        table_cards.clear() 

    game_over = True