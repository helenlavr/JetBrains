''''
n = int(input())
my_list = []
for i in range(n):
    my_list.append([])
    for j in range(1, 3):
        my_list[i].append(j)
print(my_list)
'''
# or
n = int(input())
my_list = [1, 2]
nested_list = [my_list for n in range(n)]
print(nested_list)


