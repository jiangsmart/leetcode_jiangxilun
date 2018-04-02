import sort

print "start"
nums = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
s = sort.solution()
s.quicksort(nums, 0, tail=len(nums))
print nums
