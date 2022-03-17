# Everyone Counts - Python
# Shawnak Samaddar 



x = int (input('Enter your number:'))

y = str (bin(x))

total = 0
for num in y:
    if num == '1':
        total = total+1
    else:
        pass

print ('The binary representation of contains {} 1s.'.format(total))