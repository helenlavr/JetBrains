height = int(input())
end_pyramid = height * 2 - 1
i = 1
while i <= end_pyramid:
    print(('#' * i).center(end_pyramid))
    i += 2
