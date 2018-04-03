import math as m

street_num = int(raw_input())
streets = []
for i in range(street_num):
    length = raw_input()
    street = raw_input()
    pair = (length, street)
    streets.append(pair)

for pair in streets:
    length = pair[0]
    street = pair[1]
    parts = street.split('XX')
    num = 0
    for part in parts:
        part = part.strip('X')
        if part == "":
            continue
        num += m.ceil(len(part) / 3.0)
    num = int(num)
    print num