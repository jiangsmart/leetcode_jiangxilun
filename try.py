# import bisect as b
#
# a = [1, 2, 3, 3, 3, 4]
# l = b.bisect_left(a, 3)
# r = b.bisect_right(a, 3)
# print(l, r)
# #a.insert(2, 100)
# print range(6)
# print a


# def f(a=[]):
#     a.append(1)
#     print a
#
# f([])
# f([])
# f([])
# f()
# f()
# f()

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