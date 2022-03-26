x = input('First sentence:')
y = input ('Second sentence:')
sum1 = ''
sum2 = ''

for i in x.split(sep = ' '):
    length = len (i)
    new = str(length)
    sum1 += new


for i in y.split(sep = ' '):
    length = len (i)
    new = str(length)
    sum2 += new

print (sum1 + sum2)

