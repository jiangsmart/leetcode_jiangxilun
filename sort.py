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

# 归并排序
nums2 = nums[:]
insert_sort(nums2)
# quicksort(nums2, tail=len(nums))
print nums
print nums2
