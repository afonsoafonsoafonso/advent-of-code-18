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

def checkNoOverlaps(matrix, claims, n_claims):
    for n in range(0, n_claims):
        noOverlap = True
        x = int(claims[n][1])
        y = int(claims[n][2])
        width = int(claims[n][3])
        height = int(claims[n][4])

        for i in range(x, x+width):
            for j in range(y, y+height):
                if matrix[i][j]!=1:
                    noOverlap = False

        if noOverlap == True:
            return claims[n][0]
#main
try:
    with open("input.txt", 'r') as input_file:
        lines = input_file.readlines()
except:
    print("Error opening file!")
    raise SystemExit

fabric = make_fabric_matrix()
claims = []

n_claims = len(lines)
for i in range(0,n_claims):
    claims.append(claim_parser(lines[i]))
    fabric = fabric_marker(claims[i], fabric)

print(f"No-overlap claim's ID: {checkNoOverlaps(fabric, claims, n_claims)}")