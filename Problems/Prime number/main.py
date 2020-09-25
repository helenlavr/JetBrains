number = int(input())
n = 2
if number > 0:
    if number == 1:
        print('This number is not prime')
    else:
        while n < number:
            if number % n == 0:
                print('This number is not prime')
                break
            n += 1
        else:
            print('This number is prime')

"""
number = int(input())
i = 1
count = 0
while i <= number:
    if num % i == 0:
        count += 1
    i += 1
if counter == 2:
    print('This number is prime')
else:
    print('This number is not prime')
"""
