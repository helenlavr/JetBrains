# put your python code here
grades = input().split()
result = grades.count('A')
number = result / len(grades)
print(round(number, 2))
'''
# Trenger en counter som teller antall A fra input
# Antall A i input må så deles len(input)
def proportion_students_A(grade, symbol):
    counting_A = 0
    for i in range(len(grade)):
        counting_A += grade[i].count(symbol)
    number = counting_A / len(grade)
    return round(number, 2)
    print(counting_A)

students_mark = input().split()
print(proportion_students_A(students_mark, 'A'))
'''
