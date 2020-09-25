number = [int(i) for i in input()]
digits_dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

for i in number:
    if i in digits_dic:
        digits = digits_dic.get(i)
        print(digits)
