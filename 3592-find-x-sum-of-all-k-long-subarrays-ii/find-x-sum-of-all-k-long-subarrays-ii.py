from sortedcontainers import SortedList
class Solution:
    def findXSum(self, nums: List[int], x: int, k: int) -> List[int]:
        c = Counter()
        lst = SortedList(key = lambda x : [-c[x],-x])
        self.top_k_sum = 0
        def add(num):
            lst.add(num)
            ind = lst.bisect_left(num)
            if ind <= k - 1:
                self.top_k_sum += num*c[num]
                if len(lst) >= k + 1:
                    self.top_k_sum -= lst[k]*c[lst[k]]
            return

        def discard(num):
            ind = lst.bisect_left(num)
            lst.discard(num)
            if ind <= k - 1:
                self.top_k_sum -= num*(c[num])
                if len(lst) >= k:
                    self.top_k_sum += lst[k - 1]*c[lst[k - 1]]
            return
        for num in nums[:x]:
            discard(num)
            c[num]+=1
            add(num)
        ans = [self.top_k_sum]
        for i in range(x,len(nums)):
            discard(nums[i-x])
            c[nums[i-x]]-=1
            if c[nums[i-x]]>0 :add(nums[i-x])
            discard(nums[i])
            c[nums[i]]+=1
            add(nums[i])
            ans.append(self.top_k_sum)
        return ans
            

        