two_x = 0
three_x = 0
char_count = dict()

try:
    with open("input.txt",'r') as input_file:
        for line in input_file:
            char_count.clear()
            for char in line[0:len(line)-1:]:
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1
            print(f"DICT: {char_count}")
            if 3 in char_count.keys():
                three_x += 1
            if 2 in char_count.keys():
                two_x += 1         
except:
    print("Error opening file!")
    raise SystemExit

checksum = two_x * three_x
print(f"checksum: {checksum}")