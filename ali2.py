import sys


def quanpailie(arr, res):
    history = []
    pailie2(arr, history, res)
    return


def pailie2(edges, history, res):
    res.append(history[:])
    if edges == []:
        return
    for i, edge in enumerate(edges):
        temp = edges[:]
        if history == []:
            pailie2(temp, list(edge[:]), res)
        elif edge[0] == history[-1]:
            temp.pop(i)
            pailie2(temp, history[:] + [edge[-1]], res)
    return


if __name__ == '__main__':
    _ = sys.stdin.readline()
    num = int(sys.stdin.readline().split(' ')[0])
    lines = []
    for i in range(num):
        lines.append(sys.stdin.readline())
    arr = []
    for line in lines:
        arr.append(map(int, line.split(' ')))
    paths = []
    quanpailie(arr, paths)
    paths = paths[1:]
    num_st_point = {}
    for path in paths:
        if path[0] in num_st_point:
            num_st_point[path[0]] += 1.0
        else:
            num_st_point[path[0]] = 1.0
    max_num = 0
    for st_point in num_st_point:
        max_num = max(num_st_point[st_point], max_num)
    print int(max_num)