# How many lines of number values
n = int(input())
for numbers in range(n):
    numbers = int(input())
    if numbers % 7 == 0:
        print(numbers**2)
