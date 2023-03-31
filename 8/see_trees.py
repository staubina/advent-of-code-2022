input = open('input.txt').read().split("\n")

def check_right(tree_size, x, y, tree_farm):
    max_x = len(tree_farm[y])
    if x == max_x-1:
        return True
    next = tree_farm[y][x+1]
    if next >= tree_size:
        return False
    elif next < tree_size:
        return check_right(tree_size, x+1, y, tree_farm)
    
def check_down(tree_size, x, y, tree_farm):
    max_y = len(tree_farm)
    if y == max_y-1:
        return True
    next = tree_farm[y+1][x]
    if next >= tree_size:
        return False
    elif next < tree_size:
        return check_down(tree_size, x, y+1, tree_farm)
    
def check_up(tree_size, x, y, tree_farm):
    if y == 0:
        return True
    next = tree_farm[y-1][x]
    if next >= tree_size:
        return False
    elif next < tree_size:
        return check_up(tree_size, x, y-1, tree_farm)
    
def check_left(tree_size, x, y, tree_farm):
    if x == 0:
        return True
    next = tree_farm[y][x-1]
    if next >= tree_size:
        return False
    elif next < tree_size:
        return check_left(tree_size, x-1, y, tree_farm)

# process input
tree_farm = []
current_row = 0
for row in input:
    tree_farm.append([int(tree) for tree in row])

def get_visible_tree_count(tree_farm):
    visible_tree_count = 0
    for idy, row in enumerate(tree_farm):
        for idx, tree in enumerate(row):
            if check_up(tree, idx, idy, tree_farm):
                visible_tree_count += 1
            elif check_down(tree, idx, idy, tree_farm):
                visible_tree_count += 1
            elif check_right(tree, idx, idy, tree_farm):
                visible_tree_count += 1
            elif check_left(tree, idx, idy, tree_farm):
                visible_tree_count += 1
    return visible_tree_count

print(get_visible_tree_count(tree_farm))