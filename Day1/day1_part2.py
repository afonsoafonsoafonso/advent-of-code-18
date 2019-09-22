current_frequency = 0
frequency_log = set()

while True:
    with open('input.txt') as inputfile:
        for line in inputfile:

            if line[0]=='+':
                current_frequency += int(line[1::])
            else:
                current_frequency -= int(line[1::])

            if current_frequency in frequency_log:
                print(current_frequency)
                quit()
            else:
                frequency_log.add(current_frequency)