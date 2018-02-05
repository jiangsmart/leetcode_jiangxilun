# coding=utf-8
nums = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]


def maopao(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def xuanze(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 快排

def quicksort(arr, head=0, tail=0):
    if head < tail - 1:
        middle = partition(arr, head, tail)
        quicksort(arr, head, middle)
        quicksort(arr, middle + 1, tail)
    else:
        return


def partition(arr, head, tail):
    i = head - 1
    for j in range(head, tail - 1):
        if arr[j] < arr[tail - 1]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    # 经历过上步的循环后，i+1指向的一定是比tail-1指向的数大的数，所以下一步可以和tail-1放心交换
    arr[i + 1], arr[tail - 1] = arr[tail - 1], arr[i + 1]
    return i + 1
    # 返回的是middle的位置，这个位置已经排好序了，所以下一步的partition不应该取到这个位置，
    # 下个partition只应该管到middle-1的位置


# 插入排序
def insert_sort(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            j -= 1
    return


# 希尔排序

#归并排序
def merge_sort(arr):
    length = len(arr)
    if length > 1:
        mid = length / 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    else:
        return arr


def merge(arr1, arr2):
    # if arr1 is None:
    #     return arr2
    # if arr2 is None:
    #     return arr1
    res = []
    length1 = len(arr1)
    length2 = len(arr2)
    i1, i2 = 0, 0
    while i1 < length1 and i2 < length2:
        if arr1[i1] <= arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
        else:
            res.append(arr2[i2])
            i2 += 1
    if not i1 < length1:
        while i2 < length2:
            res.append(arr2[i2])
            i2 += 1
    elif not i2 < length2:
        while i1 < length1:
            res.append(arr1[i1])
            i1 += 1
    return res
# def merge(left, right):
#     i, j = 0, 0
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
#
#
# def merge_sort(lists):
#     # 归并排序
#     if len(lists) <= 1:
#         return lists
#     num = len(lists) / 2
#     print len(lists)
#     print num
#     left = merge_sort(lists[:num])
#     right = merge_sort(lists[num:])
#     return merge(left, right)



nums2 = nums[:]
nums2 = merge_sort(nums2)
# insert_sort(nums2)
# quicksort(nums2, tail=len(nums))
print "nums:"
print nums
print "nums2:"
print nums2

