start = int(input('Enter a number:'))
final = start
even = str(start/2)
slice = even[-1]
step = 0


while  float(final) != 1.0:
    if slice == '0':
        final = final/2
        thing = final/2
        some = str (float(thing))
        slice = some[-1]

    else:
        final = (final*3) + 1
        thing = final/2
        some = str(float(thing))
        slice = some[-1]
    
    step = step + 1

print (step)