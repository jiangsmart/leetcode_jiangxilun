x=1001
if x < 0:
    print False
p = x
q = 0
while p >= 10:
    q = q * 10 + p % 10
    p /= 10
print p,q
if p == x % 10 and q == x / 10:
    print True
else:
    print False