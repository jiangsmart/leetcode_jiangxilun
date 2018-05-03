numbers=[1,2,3,2,2,2,5,4,2]
num = 0
sum_num = 0
all_sum = 0
for i in numbers:
    if sum_num == 0:
        num = i
        sum_num = 1
    else:
        if num == i:
            sum_num += 1
        else:
            sum_num -= 1
print num
for i in numbers:
    if i == num:
        all_sum += 1

if all_sum > len(numbers)/2.0:
    print num
else:
    print 0