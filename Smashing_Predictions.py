import math 

def noun (word):
    thing = 0
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i=='o' or i=='u':
            thing += 1
        else:
            pass
    
    return thing

char1, lf1 = input('First Smash Bros Character and LF:').split(sep = ' ')
char2, lf2 = input('Second Smash Bros Character and LF:').split(sep = ' ')

lf1 = float(lf1)
lf2 = float(lf2)
len1 = len(char1)
len2 = len(char2)
v1 = noun(char1)
v2 = noun (char2)

score1 = round((math.pow(len1-v1 , 2)) + ((lf1*len1)/v1), 2)
score2 = round((math.pow(len2-v2 , 2)) + ((lf2*len2)/v2), 2)

print ('{} scored {}'.format(char1, score1))
print ('{} scored {}'.format(char2, score2))

if score1>score2:
    print('{} wins!'.format(char1))

elif score1<score2:
    print ('{} wins!'.format(char2))

elif score1 == score2:
    print ('Tie!')

else:
    pass