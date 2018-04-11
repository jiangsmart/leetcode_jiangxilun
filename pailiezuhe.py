def fun(arr, sum, res):
    arr.sort()
    history = []
    findsum(arr, sum, 0, history, res)


def findsum(arr, sum, index, history, res):
    for i in range(index, len(arr)):
        if arr[i] < sum:
            findsum(arr, sum - arr[i], i + 1, history + [arr[i]], res)
        elif arr[i] == sum:
            res.append(history[:] + [arr[i]])
            return
        else:
            return
    return


def quanzuhe(arr, res):
    history = []
    index = 0
    arr.sort()
    zuhe(arr, history, res, 0)
    return


def zuhe(arr, history, res, index):
    for i in range(index, len(arr)):
        res.append(history[:] + [arr[i]])
        zuhe(arr, history[:] + [arr[i]], res, i + 1)
    return


def quanpailie(arr, res):
    history = []
    index = 0
    arr.sort()
    pailie2(arr, history, res)
    return


def pailie(arr, history, res):
    if arr == []:
        res.append(history[:])
        return
    for i in range(len(arr)):
        temp = arr[:]
        temp.pop(i)
        pailie(temp, history + [arr[i]], res)
    return


def pailie2(arr, history, res):
    res.append(history[:])
    if arr == []:
        return
    for i in range(len(arr)):
        temp = arr[:]
        temp.pop(i)
        pailie2(temp, history + [arr[i]], res)
    return


res = []
nums = range(3)
# fun([nums, 30, res)
# quanzuhe(nums, res)
quanpailie(nums, res)
print res
print len(res)
