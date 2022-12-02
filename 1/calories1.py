elf_file = open('test_data2.txt')
calorie_list = elf_file.read().split('\n')
elf_calorie_data = [0]
elf = 0
for calorie in calorie_list:
    if calorie == '' and elf < len(elf_calorie_data):
        print(f'elf {elf}: {elf_calorie_data[elf]}')
        elf += 1
        elf_calorie_data.append(0)
    else:
        elf_calorie_data[elf] += int(calorie)

elf_max = max(elf_calorie_data)
print(f'Elf with max load is {elf_calorie_data.index(elf_max)} and Calorie load is {elf_max}')