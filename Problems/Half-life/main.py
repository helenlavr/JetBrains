"""
half-line_periods: 12 days --> int(atom * 1/2)
1: initial_quantity of atoms from input
2: final_quantity -"-
3: count #half-line_periods it takes to go below final quantity
4: half_line_multiplied_12 = (#half-line_periods * 12) --> convert to days: half_line_multiplied_12 // 24
5: output: #days it takes for initial_quantity to go below final_quantity
"""
amount_of_quantity = int(input())
final_quantity = int(input())

count = 0
while amount_of_quantity >= final_quantity:
    amount_of_quantity = amount_of_quantity // 2
    count += 1

print(count * 12)
