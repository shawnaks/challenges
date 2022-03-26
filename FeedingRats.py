n = int(input('Number of rats/cheese'))
rats = input('Rats:').split(' ', n)
cheese = input('Cheese:').split(' ', n)
hungry = 0
pound = 0
new_rats = []
new_cheese = []

for i in rats:
    var = int(i)
    new_rats.append(var)

for i in cheese:
    var = int(i)
    new_cheese.append(var)

new_rats = sorted (new_rats, reverse=True)
new_cheese = sorted (new_cheese, reverse=True)

for i in range (n):
    x,y = new_rats[i-1], new_cheese[i-1]
    if y > x :
        sto = y-x
        pound += sto

    if x < y:
        sto = 0
        hungry += 1
    
    if x == y:
        sto = 0


print ('{} pound(s) left over, {} hungry rats'.format(pound,hungry))