import random, sys
print('Do you want a random number between 1-10')
print('Please type yes or no')
answer = input()
realAnswer = answer.lower()
while realAnswer == 'yes':
            print(random.randint(1,10))
            print('would you like another random number yes or no')
            answer = input()
            realAnswer = answer.lower()
            

print('No number for you')
sys.exit()
            
            



