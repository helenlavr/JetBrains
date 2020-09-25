"""
import numpy as np
#Evt på denne myyye lettere måten:
number = list(input())
number_list = [int(i) for i in number]
cumulative_sum = list(np.cumsum(number_list))
print(cumulative_sum)
"""


number = list(input())
number_list = [int(i) for i in number]

result_list = []
s = 0
for item in number_list:
    s += item
    result_list.append(s)
print(result_list)

