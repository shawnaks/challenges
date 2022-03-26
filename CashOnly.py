import math
total = input ('Total:')
given = input('Cash given:')
cash = 0
needed = ''

for i in given:
    if i == '5':
        cash += 5
    if i == '1':
        cash += 1
    if i == 'Q':
        cash += .25
    if i == 'D':
        cash += .1
    if i == 'N':
        cash += .05
    if i == 'P':
        cash += .01

if cash == total:
    print ('Clerk response: Thank you for your exact purchase.')

elif cash < total:
    print ('Clerk response: This is not enough cash to make this purchase.')

elif cash > total:
    cash *= 100
    remain = cash-total
    coins = {500 : 0, 100 : 0 , 25 : 0 , 10 : 0 , 5: 0 , 1 : 0}
    for i in coins.keys():
        for i in range ((math.floor(remain/i)):
            
        remain = remain % 500
