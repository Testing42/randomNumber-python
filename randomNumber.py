import random, sys
count = 0
print('Do you want a random number between 1-10')
print('Please type yes or no')
answer = input()
if answer == 'yes':
  print(random.randint(1,10))
elif answer == 'no':
  print('No number for you')
else:
  print('Please type yes or no')
  answer = input()
  while answer != 'yes' or answer != 'no':
            print('Please type yes or no')
            answer = input()
            if answer == 'yes':
              print(random.randint(1,10))
              sys.exit()
            elif answer == 'no':
              print('No number for you')
              sys.exit()
            
            



