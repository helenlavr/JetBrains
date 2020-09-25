name_list = []
while True:
    name_input = input()
    if name_input != '.':
        name_list.append(name_input)
    else:
        break

participants = len(name_list)
print(name_list)
print(participants)
