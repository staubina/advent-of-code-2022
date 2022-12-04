rucksack_list = open('input.txt').read().split("\n")
print(rucksack_list)

mispacked_score = 0
for rucksack in rucksack_list:
    print(rucksack)
    mid = int(len(rucksack)/2)
    compartment1 = rucksack[:mid]
    compartment2 = rucksack[mid:]
    shared = set(compartment1).intersection(compartment2).pop()
    if shared.islower():
        mispacked_score += ord(shared) - 96
    else:
        mispacked_score += ord(shared) - 38
print(f'Final Score {mispacked_score}')