digits_list = list(input())
int_list = [int(i) for i in digits_list]
mean_ = sum(int_list) / len(int_list)
print(mean_)
