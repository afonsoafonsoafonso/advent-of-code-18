def check_difference(id1, id2):
    diff_count = 0
    
    for i in range(0,len(id1)):
        if id1[i] != id2[i]:
            diff_count += 1
            diff_index = i

        if diff_count > 1:
            return False

    if diff_count == 1:
        print(f"DIFF_INDEX: {diff_index}")
        id1 = id1[0:diff_index:] + id1[diff_index+1::]
        print(id1)
        return True

    return False

try:
    with open("input.txt",'r') as input_file:
        ids = input_file.readlines()
except:       
    print("Error opening file!")
    raise SystemExit

n_ids = len(ids)
for i in range(0,n_ids):
    for j in range(i,n_ids):
        if check_difference(ids[i], ids[j]) == True:
            quit()
        else:
            continue