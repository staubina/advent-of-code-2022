import re

CRATE_REGEX = "\[(.*?)\]|\s\s\s\s(?!\d)"
crane_orders = open('puzzle_input.txt').read().split("\n")
levels = []
stack_count = 0;
current_stack = crane_orders.pop(0)
# Get Current State
# for stack in crane_orders:
print("GET STACKS")
while current_stack != '':
    print(f'current: {current_stack}')

    crates = re.findall(CRATE_REGEX, current_stack)
    stack_count_row = re.findall("\d", current_stack)
    if crates != []:
        levels.append(crates)
    current_stack = crane_orders.pop(0)

# Build Stacks
supply_floor = {}
supply_stacks = len(levels[0])
for level in levels:
    for idx, crate in enumerate(level):
        if crate == '':
            continue
            # Skip empty spots
        if idx in supply_floor:
            supply_floor[idx].append(crate)
        else: 
            supply_floor[idx] = [crate]
print("Levels")
print(levels)
print('\n')
print('Supply Floor')
print(supply_floor)
print('\n')

# Get Steps
# move 1 from 2 to 1
# [move #, from, to]
print("GET STEPS")
executable_orders = []
for step in crane_orders:
    current_step = [int(i) for i in re.findall("\d+", step)]
    executable_orders.append(current_step)
print(executable_orders)
print('\n')

# Execute orders
for order in executable_orders:
    move_count, from_stack, to_stack = order
    from_crates = []
    for m in range(move_count):
        if supply_floor[from_stack-1]:
            from_crates.append(supply_floor[from_stack-1].pop(0))
            # supply_floor[to_stack-1].insert(0, from_crate)
    supply_floor[to_stack-1][0:0] = from_crates
print(supply_floor)
print('\n')

print("RESULT")
result = ''
for idx in range(supply_stacks):
    value = supply_floor.get(idx)
    if value:
        result += value[0]
print(result)