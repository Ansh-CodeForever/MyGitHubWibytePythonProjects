import time
import random
import datetime as dt
import os
import tt
import pyfiglet

class BadLetterError(Exception):
  def __init__(self, message = 'Some of those letters should be avoided'):
    self.message = message
    super().__init__(message)
  pass

class BadTimeError(Exception):
  pass

def short_form(idx, *names, **addons):
  final = ''

  try:
    for name in names:
      final = final + name[idx]
    for keys in addons:
      if keys == 'prefix':
        final = addons[keys] + final
      elif keys == 'suffix':
        final = final + addons[keys]
      else:
        print('You are not good at typing, are you ...')
        
  except TypeError as e:
    print('Wrong data type: ', e)
  except IndexError as e:
    print('Indexing is going wrong:', e)
  except Exception as e:
    print('Something went wrong', e)
  else:
    return final
  finally:
    print("Hope you managed to pass this stage ...")
    
strength = {'name':10, 'surname':20, 'nickname': 30, 'alias': 40, 'aka':50}
  
def name_strength(**fullname):
  result = 0
  try:
    for key, value in fullname.items():
      result += strength[key]*len(value)
  except KeyError as e:
    print('Perhaps you are providing too much info', e)
  except Exception as e:
    print('Something went wrong', e)
  else: 
    return result
  finally:
    print('Hopefully this satge was easy to...')

def tell_me_a_word():
  common_words = ['welcome', 'welcoming', 'welcomed', 'lovely', 'kind', 'beatiful']
  topic = ['welcoming', 'nice', 'interesting']
  which_topic = random.choice(topic)
  try:
    print('Tell me a', which_topic, 'word:')
    tellword = input()
    if ' ' in tellword:
      print('I asked you for 1 word')
    elif len(tellword) > 11:  
      print('I am bord of reading your nonsense')
    elif tellword in common_words:
      print('To common, can\'t you think of something better')
    elif tellword.lower() == 'ansh':
      print('Magic word! You Pass')
      return tellword
    else:
      print('This should have been easy...')
      return tellword
  except ValueError:
    print('You thought I couldn\'t catch numbers or symbols...')

def guess_number(num1, num2):
  attempts = 0
  try:
    usless_help = ['Your 73% there!', 'You are correct but incorrect', 'You are hot but cold', 'Keep it up and you will get there']
    if num1 > num2:
      print('2nd number should be larger')
    elif (num2 - num1) < 50:
      print('Gap is to small, should be atleast 50')
    chosen_number = random.randint(num1, num2)
    end = 0
    while end == 0:
      enter = int(input('What is your guess\n'))
      if enter > chosen_number:
        print('Too large')
        attempts += 1
        end = 0
      elif enter < chosen_number:
        print('Too small')
        attempts += 1
        end = 0
      else:
        print('You Guessed it, you neede', attempts, 'guesses!')
        if attempts %4 == 0:
          pass
        end = 1 
      if attempts % 4 == 0:
        print(random.choice(usless_help))
  except Exception as e:
    print('Something went wrong...', e)
  finally:
    return attempts  

def validate(**prelimdata):
  print(prelimdata)
  print('Validating...')

  rejections = ["Nope. Try again, mortal.",
    "That name is banned in 37 countries.",
    "Too cool for this program. Pick something lamer.",
    "Validation failed. But your effort was adorable.",
    "Out of luck mate, try again next time",
    "Computer says no. 🤖"]
  
  time.sleep(1)
  try:
    assert prelimdata['sc'] != None
    assert prelimdata['ns'] != None
    assert prelimdata['tw'] != None
    assert prelimdata['gn'] != None
  except KeyError as e:
    print('You are really bad at typing, aren\'t you?')
    print('Validation failed due to ', e)
    tt.validation_failed()
    os._exit(1)
  except AssertionError:
    print('One of the earlier steps has gone wrong.')
    print('Validation failed')
    tt.validation_failed()
    os._exit(1)
  else:
    print('Looking good so far ...')
    print('Sending for deeper validation')
    print('opening connection to a remote server ...')
    try:
      # this is based on luck
      deep_validate(prelimdata)
      print('Deep Validation check...')
      time.sleep(1.5)
    except ValueError:
      print('There is something deeply wrong')
      print('Validation failed...')
      print(random.choice(rejections))
      tt.validation_failed()
      os._exit(1)
    except BadLetterError as e:
      print('I did not like some of the letters you used in the short code...', e)
      print('Validation failed...')
      print(random.choice(rejections))
      tt.validation_failed()
      os._exit(1)
    except BadTimeError as e:
      print('Cannot conect to server right now, please try again later...')
      print('Validation failed...')
      print(random.choice(rejections))
      tt.validation_failed()
      os._exit(1)
    else:
      print('Congrats... Validation Successful')
      print('Welcome to my world, We need a party!')
      name = input('What is your name: ')
      art = pyfiglet.figlet_format(name)
      print('🎉🎉🎉 WELCOME, HERO OF LEGEND', name, '! 🎉🎉🎉')
      print("The prophecy foretold your arrival...")
      print(art)
    finally:
      print('Closing connection to the remote server')

def deep_validate(prelimdata):
  print(prelimdata)

  threshold_ns = random.randint(1, 200)
  threshold_sc = random.randint(10, 20)
  threshold_tw = random.randint(2, 18)
  threshold_gn = random.randint(1, 100)

  print()
  print('Conecting to server...', threshold_ns, threshold_sc, threshold_tw, threshold_gn)
  time.sleep(2)
  print()

  badletters = ['b', 'd', 'x']

  ct = dt.datetime.now()
  if ct.second % 5 == 0:
    raise BadTimeError

  if any(x in prelimdata['sc'] for x in badletters):
    raise BadLetterError('Avoid, b, d, r and x')
  
  if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc or len(prelimdata['tw']) > threshold_tw or prelimdata['gn'] > threshold_gn:
    raise ValueError

print('Welcome to the Programmers\' Den')
print("I hear you have been learning Python")
print('Guess you can use the command line to create your own welcome kit')
print()
print('You might want to read the README file for clearer instructions.')
print('If you are lazy, I have alredy put some instructions here as well.')
print()
print('The process is simple, create a short code, check your name strength and then validate')
print('For short code, use sc = short_form(idx, a few words about youself, prefix = , suffix = ')
print('For name strength code, use ns = name_strength(name =, surname = , aka = , alias = , salutation = ')
print('For validate, use validate (sc = sc, ns = ns)')
print('Alright champ, get going ...')
print(' ')