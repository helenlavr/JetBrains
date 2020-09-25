number = int(input())
counter = 1
while number > 0:
    counter *= number
    number -= 1
print(counter)
