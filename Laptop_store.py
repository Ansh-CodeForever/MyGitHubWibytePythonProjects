import random

print('Welcome to my laptop store, called digipro! We have lot\'s of computers, choose your prefence!')
print()

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']
laptop = dict.fromkeys(specs)

master_dict = {}
master_dict['Brands'] = ['WDell', 'WLenovo', 'WMac', 'WAcer', 'WAcus', 'WHP', 'Apple']
master_dict['Models'] = ['WIntel i5', 'WIntel i7', 'Wamd Ryzen']
master_dict['CPUs'] = ['WDell', 'WLenovo', 'WMac', 'WAcer', 'WAcus', 'WHP']
master_dict['Speeds'] = ['900 MHz', '2 GHz', '3 GHz', '', '4.5 GHZ']
master_dict['RAMs'] = ['1 GB', '2 GB', '2.5 GB', '4 GB', '6.5 GB', '8 GB']
master_dict['Storages'] = ['128 GB', '226 GB', '546 GB', '750 GB', '867 GB', '1 TB']
master_dict['Screensizes'] = ['9 in', '12 in', '13 in', '14.9 in', '15.5 in', '17 in']
master_dict['Prices'] = ['EUR', random.randint(500, 800)]

laptop_list = []
n_laptops = 50

for _ in range(n_laptops):
    new_laptop = dict.fromkeys(specs)
    for kk in new_laptop:
        new_laptop[kk] = random.choice(master_dict[kk+'s'])
    laptop_list.append(new_laptop)

user_choice = dict.fromkeys(specs)
for kk in specs:
    user_choice[kk] = input('Any prefernce for ' + kk + '(Enter \'enter\' for no prefernce)\n')

querry = ''
for kk in user_choice:
    if user_choice[kk].lower() == '':
        pass
    else:
        querry = querry + 'laptop[' + '\'' + kk + '\'' + '] == ' + '\'' + kk + '\'' + ' and '

