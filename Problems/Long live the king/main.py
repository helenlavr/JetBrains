column = int(input())
row = int(input())

if (column == 1 and row == 1) or (column == 1 and row == 8) or (column == 8 and row == 8) or (column == 8 and row == 1):
    print('3')
elif (column == 1 and row == 2) or (column == 1 and row == 3) or (column == 1 and row == 4) or (column == 1 and row == 5) or (column == 1 and row == 6) or (column == 1 and row == 7):
    print('5')
elif (column == 2 and row == 1) or (column == 3 and row == 1) or (column == 4 and row == 1) or (column == 5 and row == 1) or (column == 6 and row == 1) or (column == 7 and row == 1):
    print('5')
elif (column == 8 and row == 2) or (column == 8 and row == 3) or (column == 8 and row == 4) or (column == 8 and row == 5) or (column == 8 and row == 6) or (column == 8 and row == 7):
    print('5')
elif (column == 2 and row == 8) or (column == 3 and row == 8) or (column == 4 and row == 8) or (column == 5 and row == 8) or (column == 6 and row == 8) or (column == 7 and row == 8):
    print('5')
else:
    print('8')

###
# or much simpler
# x = int(input())
# y = int(input())
#
# if x in (1, 8) and y in (1, 8):
#     print(3)
# elif x in (1, 8) or y in (1, 8):
#     print(5)
# else:
#     print(8)

