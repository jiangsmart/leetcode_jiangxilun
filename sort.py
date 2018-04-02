# coding=utf-8

class solution():
    def maopao(self, arr):
        length = len(arr)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def xuanze(self, arr):
        length = len(arr)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    # 快排

    def quicksort(self, arr, head=0, tail=0):
        if head < tail - 1:
            middle = self.partition(arr, head, tail)
            self.quicksort(arr, head, middle)
            self.quicksort(arr, middle + 1, tail)
        else:
            return

    # def partition(arr, head, tail):
    #     i = head - 1
    #     for j in range(head, tail - 1):
    #         if arr[j] < arr[tail - 1]:
    #             i += 1
    #             arr[j], arr[i] = arr[i], arr[j]
    #     # 经历过上步的循环后，i+1指向的一定是比tail-1指向的数大的数，所以下一步可以和tail-1放心交换
    #     arr[i + 1], arr[tail - 1] = arr[tail - 1], arr[i + 1]
    #     return i + 1
    #     # 返回的是middle的位置，这个位置已经排好序了，所以下一步的partition不应该取到这个位置，
    #     # 下个partition只应该管到middle-1的位置

    def partition(self, arr, head, tail):
        j = head
        for i in range(head, tail - 1):
            if arr[i] < arr[tail - 1]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[j], arr[tail - 1] = arr[tail - 1], arr[j]
        return j

    # 插入排序
    def insert_sort(self, arr):
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
    def merge_sort(self, arr):
        length = len(arr)
        if length > 1:
            mid = length / 2
            left = self.merge_sort(arr[:mid])
            right = self.merge_sort(arr[mid:])
            return self.merge(left, right)
        else:
            return arr

    def merge(self, arr1, arr2):
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
        res += arr1[i1:]
        res += arr2[i2:]
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


if __name__ == "__main__":
    s = solution()
    nums = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
    nums2 = nums[:]
    s.quicksort(nums2, head=0, tail=len(nums))
    print "nums:"
    print nums
    print "nums2:"
    print nums2
