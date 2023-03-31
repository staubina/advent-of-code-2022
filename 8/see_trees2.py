def check_right(tree_size, x, y, tree_farm, count):
    max_x = len(tree_farm[y])
    if x == max_x-1:
        return count
    next = tree_farm[y][x+1]
    if next >= tree_size:
        count += 1
        return count
    elif next < tree_size:
        count += 1
        return check_right(tree_size, x+1, y, tree_farm, count)
    
def check_down(tree_size, x, y, tree_farm, count):
    max_y = len(tree_farm)
    if y == max_y-1:
        return count
    next = tree_farm[y+1][x]
    if next >= tree_size:
        count += 1
        return count
    elif next < tree_size:
        count += 1
        return check_down(tree_size, x, y+1, tree_farm, count)
    
def check_up(tree_size, x, y, tree_farm, count):
    if y == 0:
        return count
    next = tree_farm[y-1][x]
    if next >= tree_size:
        count += 1
        return count
    elif next < tree_size:
        count += 1
        return check_up(tree_size, x, y-1, tree_farm, count)
    
def check_left(tree_size, x, y, tree_farm, count):
    if x == 0:
        return count
    next = tree_farm[y][x-1]
    if next >= tree_size:
        count+=1
        return count
    elif next < tree_size:
        count+=1
        return check_left(tree_size, x-1, y, tree_farm, count)

# process input
input = open('input2.txt').read().split("\n")

tree_farm = []
current_row = 0
for row in input:
    tree_farm.append([int(tree) for tree in row])

def get_tree_fort_score(tree_farm):
    all_tree_vals = []
    for idy, row in enumerate(tree_farm):
        for idx, tree in enumerate(row):
            up_val = check_up(tree, idx, idy, tree_farm, 0)
            down_val = check_down(tree, idx, idy, tree_farm, 0)
            right_val = check_right(tree, idx, idy, tree_farm, 0)
            left_val = check_left(tree, idx, idy, tree_farm, 0)
            tree_val = (up_val * down_val * right_val * left_val)
            all_tree_vals.append(tree_val)
    return all_tree_vals

print(max(get_tree_fort_score(tree_farm)))