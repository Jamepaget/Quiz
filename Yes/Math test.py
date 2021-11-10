# Put questions up and get them to answer
def response(response):


#Questons and answers for quiz

 from time import time
from random import randint

while True:
    num1 = randint(2, 9)
    num2 = randint(2, 9)
    product = num1 * num2
    ans = int(input(f'what is {num1} * {num2}? '))
    if not response:
        break
    try:
        ans = int(response)
        print('Correct!' if ans == product else 'wrong')
    except ValueError:
        print('That was not a number')

