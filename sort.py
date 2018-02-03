nums = [5, 4, 3, 7, 8, 10, 9, 5, 3, 4]


def maopao(nums):
    length = len(nums)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums


def xuanze(nums):
    length = len(nums)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[j] < nums[i]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
    return nums


# def partition(nums, left, right):
#     # if left == right:
#     #     return left
#     j = right
#     i = left+1
#     while i < j:
#         while i < j and nums[j] >= nums[left]:
#             j -= 1
#         while i < j and nums[i] <= nums[left]:
#             i += 1
#         temp = nums[i]
#         nums[i] = nums[j]
#         nums[j] = temp
#     if i != left+1 and j != right:
#         temp = nums[left]
#         nums[left] = nums[j]
#         nums[j] = temp
#         return j
#     elif j == right:
#         temp = nums[left]
#         nums[left] = nums[right]
#         nums[right] = temp
#         return right
#     else: return j-1

def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        v[low] = key
    return low

def quicksort(v, left, right):
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v

# def quicksort(nums, left, right):
#     middle = partition(nums, left, right)
#     print nums
#     if left<middle-1:
#         quicksort(nums, left, middle-1)
#     if right>middle+1:
#         quicksort(nums, middle+1, right)
#     return

def kuaisu(nums):
    length = len(nums)
    return quicksort(nums, 0, length - 1)

def charu(nums):
    length=len(nums)
    if length>1:
        

#print nums
#print maopao(nums[:])
#print nums
#print xuanze(nums[:])
print nums
print kuaisu(nums[:])
