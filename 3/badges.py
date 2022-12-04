rucksack_list = open('input.txt').read().split("\n")
score = 0

for start in range(0, len(rucksack_list), 3):
    end = start + 3
    one, two, three = rucksack_list[start:end]
    shared = set(one).intersection(two, three).pop()

    if shared.islower():
        score += ord(shared) - 96
    else:
        score += ord(shared) - 38
    print(f'{one} / {two} / {three}')
    print(f'{shared}')
    print(f'\nFinal Score: {score}')