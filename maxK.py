class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput)<k or k==0:
            return []
        import bisect
        buff=tinput[:k]
        buff.sort()
        for i in tinput[k:]:
            if i<buff[-1]:
                bisect.insort(buff,i)
                buff.pop()
        return buff