n, m = map(int, raw_input().strip().split())
machs = []
tasks = []
value = []
for i in range(n):
    a, b = map(int, raw_input().strip().split())
    machs.append([a, b, 0])
for i in range(m):
    a, b = map(int, raw_input().strip().split())
    c = 200 * a + 3 * b
    tasks.append((a, b, c))
# print machs
# print tasks
mach_task = []
for mach in machs:
    value = 0
    index = -1
    for i, task in enumerate(tasks):
        # print mach[0],task[0]
        # print mach[1], task[1]
        if mach[0] >= task[0] and mach[1] >= task[1]:
            if task[2] > value:
                # print "bingo"
                value = task[2]
                index = i
    if index != -1:
        tasks.pop(index)
    # print tasks
    mach_task.append(value)
task_num = len(mach_task)
whole_value = sum(mach_task)
print task_num, whole_value
