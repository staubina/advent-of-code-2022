
cleanup_orders = open('puzzle_input.txt').read().split("\n")
fully_contained_count = 0
part_contained_count = 0

for crew in cleanup_orders:
    elf1, elf2 = crew.split(',')
    print(f'elf1: {elf1}, elf2: {elf2}')
    start_e1, end_e1 = elf1.split('-')
    start_e2, end_e2 = elf2.split('-')
    elf1_orders = [i for i in range(int(start_e1), int(end_e1)+1)]
    elf2_orders = [i for i in range(int(start_e2), int(end_e2)+1)]
    print(f'elf1: {str(elf1_orders)}, elf2: {str(elf2_orders)}')
    check_elf1 = all(order in elf2_orders for order in elf1_orders)
    check_elf2 = all(order in elf1_orders for order in elf2_orders)
    print(f'elf1: {str(check_elf1)}, elf2: {str(check_elf2)}')
    print('\n')

    if check_elf1 or check_elf2:
        fully_contained_count += 1

    # Part 2
    check_part_elf1 = any(order in elf2_orders for order in elf1_orders)
    check_part_elf2 = any(order in elf1_orders for order in elf2_orders)
    if check_part_elf1 or check_part_elf2:
        part_contained_count += 1

print(fully_contained_count)
print(part_contained_count)
