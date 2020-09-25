'''
1: count sum from 1 to k.
2: add numbers from 1 to k --> print
'''

k = int(input())
i = 1
list_of_k = []
while i <= k:
    list_of_k.append(i)
    i += 1
print(sum(list_of_k))

'''
k = int(input())
print(sum(i for i in range(1, k + 1)))
'''
