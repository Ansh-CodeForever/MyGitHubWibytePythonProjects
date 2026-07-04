import random
import colorama
from colorama import Fore, Back, Style

print('Welcome to my laptop store, called digipro! We have lot\'s of computers, choose your prefence!')
print()

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']
laptop = dict.fromkeys(specs)

master_dict = {}
master_dict['Brands'] = ['WDell', 'WLenovo', 'WMac', 'WAcer', 'WAcus', 'WHP', 'Apple']
master_dict['Models'] = ['Dell XPS 13', 'Apple MacBook Air', 'Lenovo ThinkPad X1 Crbon']
master_dict['CPUs'] = ['WIntel i5', 'WIntel i7', 'Wamd Ryzen']
master_dict['Speeds'] = ['900 MHz', '2 GHz', '3 GHz', '', '4.5 GHZ']
master_dict['RAMs'] = ['1 GB', '2 GB', '2.5 GB', '4 GB', '6.5 GB', '8 GB']
master_dict['Storages'] = ['128 GB', '226 GB', '546 GB', '750 GB', '867 GB', '1 TB']
master_dict['Screensizes'] = ['9 in', '12 in', '13 in', '14.9 in', '15.5 in', '17 in']
master_dict['Prices'] = [' EUR 550', 'EUR 600', 'EUR 700', 'EUR 750', 'EUR 800']

models = dict.fromkeys(master_dict['Brands'])
models['WDell'] = ['Inspire', 'Altitude', 'Adam']
models['WLenovo'] = ['Think', 'Idea', 'Yoga']
models['WMac'] = ['MacBook Retnia', 'MacBook Air', 'MacBook Pro']
models['WAcer'] = ['Lite', 'Aspire', 'Nitro']
models['WAcus'] = ['Vivo', 'TUF', 'Zen']
models['WHP'] = ['Mini', 'Maxima', 'Pro']
models['Apple'] = ['MacBook Air', 'MacBook Pro', 'MackBook Neo']

base_price = {'WDell': 600, 'WLenovo': 800, 'WMac': 750, 'WAcer': 600, 'WAcus': 550, 'WHP': 700, 'Apple': 850}
feature_price = {'Speed': 50, 'RAM': 95, 'Storage': 25, 'Screensize': 120}


laptop_list = []
n_laptops = 50

for n_laptops in range(50):
    new_laptop = dict.fromkeys(specs)
    for kk in new_laptop:
        if kk != 'Model':
            new_laptop[kk] = random.choice(master_dict[kk+'s'])
    new_laptop['Model'] = random.choice(models[new_laptop['Brand']])
    new_laptop['Price'] = base_price[new_laptop['Brand']]
    incr_price = 0
    for feature in feature_price:
        incr_price += master_dict[feature+'s'].index(new_laptop[feature])*feature_price[feature]

    new_price = new_laptop['Price'] + incr_price
    new_laptop['Price'] = 'EUR ' + str(new_price)
    laptop_list.append(new_laptop)

user_choice = dict.fromkeys(specs)

pref = input('Please indicate the specifications where you have a prefernce for. \nYou can specify these things: Brand, Model, CPU, Speed, RAM, Storage, Screensize, Price. (comma seperate)\n')
pref_list = pref.split(',')
pref_list = list(map(str.strip, pref_list))

units = {'Speed': 'GHz', 'RAM': 'GB', 'Storage': 'GB', 'Screensize': 'in', 'Price': 'EUR'}
for kk in specs:
    if kk in pref_list:
        if kk != 'Model':
            pref_str = '/'.join(master_dict[kk+'s'])
        else:
            pref_str = '/'.join(models[user_choice['Brand']])
        user_response = input('Your prefernce for ' + kk + ': ' + pref_str + ' (No prefernce: \'\', Multiple: Comma seperated, Range: R\n')
        if user_response == 'R':
            min = input('Minimum ' + units[kk] + ': ')
            max = input('Maximum ' + units[kk] + ': ')
            user_choice[kk] = str(min) + '-' + str(max)
        else:
            user_choice[kk] = user_response
    else:
        user_choice[kk] = ''

querry = ''
for kk in user_choice:
    if user_choice[kk].lower() == '':
        pass
    elif ',' in user_choice[kk]:
        m_choices = user_choice[kk].split(',')
        mc_list = list(map(str.strip, m_choices))
        for c in mc_list:
            if c == mc_list[0]:
                querry = querry + '(' + 'laptop[' + '\'' + kk + '\'] == ' + '\'' + c + '\'' + ' or '
            elif c != mc_list[-1]:
                querry = querry + 'laptop[' + '\'' + kk + '\'] == ' + '\'' + c + '\'' + ' or '
            else:
                querry = querry + 'laptop[' + '\'' + kk + '\'] == ' + '\'' + c + '\'' + ')' + ' and ' 
    elif '-' in user_choice[kk]:
        range_min = user_choice[kk].split('-')[0]
        range_max = user_choice[kk].split('-')[1]  
        if kk != 'Price':  
            querry = querry + '(' + 'float(laptop[' + '\'' + kk + '\'' + '].split()[0]) >= ' + range_min
            querry = querry + ' and float(laptop[' + '\'' + kk + '\'].split()[0]) <=' + range_max + ')' + ' and '
        else:
            querry = querry + '(' + 'float(laptop[' + '\'' + kk + '\'' + '].split()[0]) >= ' + range_min
            querry = querry + ' and float(laptop[' + '\'' + kk + '\'].split()[1]) <=' + range_max + ')' + ' and ' 
    else:
        querry = querry + 'laptop[' + '\'' + kk + '\'' + '] == ' + '\'' + user_choice[kk] + '\'' + ' and '
querry = querry[0:-4:1]

selected_laptops = []
if querry == '':
    selected_laptops = [laptop for laptop in laptop_list]
else:
    for laptop in laptop_list:
        if eval(querry):
            selected_laptops.append(laptop)
    selected_laptops = [laptop for laptop in laptop_list if eval(querry)]


print()
print(len(selected_laptops), ' laptops have met your prefernces')

sorting_key = input('Results to be sorted by: (none for no sorting): ')
sorting_rev = input('Enter D for desceding order, A for ascending order.')

if sorting_key == 'Brand':
    selected_laptops = sorted(selected_laptops, key = lambda x: x[sorting_key], reverse = (sorting_rev == 'D')) 
elif sorting_key == 'Price':
    selected_laptops = sorted(selected_laptops, key = lambda x: float(x[sorting_key].split()[1]), reverse = (sorting_rev == 'D')) 
elif sorting_key != 'none':
    elected_laptops = sorted(selected_laptops, key = lambda x: float(x[sorting_key].split()[0]), reverse = (sorting_rev == 'D'))
characters = 0
for kk in specs:
    print(kk, end = '')
    characters = len(kk)
    print((13-characters)*' ', end = '')
print()

characters = 0
colours = {'WDell': 'green', 'WLenovo': 'blue', 'WMac': 'yellow', 'WAcer': 'red', 'WAcus': 'magenta', 'WHP': 'cyan', 'Apple': 'white'}

for laptop in selected_laptops:
    for kk in laptop:
        print(getattr(Fore, colours[laptop['Brand']].upper()) + laptop[kk], end = '')
        characters = len(laptop[kk])
        print((13-characters)*' ', end = '')
    print()
