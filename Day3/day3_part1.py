import re

# claim[0]:id ; claim[1]:left_offset ; claim[2]:top_offset
# claim[3]:width ; claim[4]:height
def claim_parser(line):
    return re.findall('\d+',line)
    
def make_fabric_matrix():
    matrix = [[0 for x in range(1000)] for y in range(1000)]
    return matrix

def fabric_marker(claim, matrix):
    x = int(claim[1])
    y = int(claim[2])
    width = int(claim[3])
    height = int(claim[4])
    for i in range(x, x+width):
        for j in range(y, y+height):
            matrix[i][j] += 1
    return matrix

def checkOverlaps(matrix):
    count = 0
    for i in range(0,1000):
        for j in range(0,1000):
            if matrix[i][j] > 1:
                count+=1
    return count

#main
try:
    with open("input.txt", 'r') as input_file:
        claims = input_file.readlines()
except:
    print("Error opening file!")
    raise SystemExit

fabric = make_fabric_matrix()

n_claims = len(claims)
for i in range(0,n_claims):
    claim = claim_parser(claims[i])
    fabric = fabric_marker(claim, fabric)

print(f"Total no. overlaps: {checkOverlaps(fabric)}")



    









