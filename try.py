import bisect as b

a = [1, 2, 3, 3, 3, 4]
l = b.bisect_left(a, 3)
r = b.bisect_right(a, 3)
print(l, r)
#a.insert(2, 100)
print range(6)
print a