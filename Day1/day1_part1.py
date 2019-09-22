frequency = 0

with open('input.txt') as inputfile:
    for line in inputfile:
        if(line[0]=='+'):
            frequency += int(line[1::])
        else:
            frequency -= int(line[1::])

print(frequency)
