# Fibonacci - Python
# Shawnak Samaddar
# Finds whether a number is in the Fibonacci Sequence and finds the position of the number in the sequence

dict = {1:0, 2:1}
h = 0

def fibonacci(num):
    loop = num+1
    for i in range (3, loop):
        dict[i] = dict[i-1] + dict[i-2]

fibonacci (32)

iterate = list (dict.values())
input = int (input ('Enter a number:'))
 
if (input == 1) :
    print ('The number 1 in found in position 2 and 3.')


elif (input in iterate):
    for g in iterate:
        if g == input:
            h = iterate.index(input) + 1                        
            print ('The number {} is found in position {}'.format(input, h))
            break

else:
    print ('The number {} is not found in the sequence'.format(input))
