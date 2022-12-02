elf_file = open('test_data_p2.txt')
calorie_list = elf_file.read().split('\n')
elf_calorie_data = [0]
current_elf = 0

for calorie in calorie_list:
    if calorie == '' and current_elf < len(elf_calorie_data):
        print(f'elf {current_elf}: {elf_calorie_data[current_elf]}')

        current_elf += 1
        elf_calorie_data.append(0)
    else:
        elf_calorie_data[current_elf] += int(calorie)

elf_max = max(elf_calorie_data)
print(f'Elf with max load is {elf_calorie_data.index(elf_max)} and Calorie load is {elf_max}')
elf_calorie_data.sort(reverse=True)
print(f'elf1: {elf_calorie_data[0]}, elf2: {elf_calorie_data[1]}, elf3: {elf_calorie_data[2]}')
print(f'Total carried {sum(elf_calorie_data[0:3])}')