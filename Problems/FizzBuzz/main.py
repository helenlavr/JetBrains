for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = str('FizzBuzz')
    elif i % 3 == 0:
        i = str('Fizz')
    elif i % 5 == 0:
        i = str('Buzz')
    print(i)
