class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        res = sorted(nums)
        hmap = defaultdict(int)
        q_list = [deque([res[0]])]
        hmap[res[0]], group, n = 0, 0, len(nums)

        for i in range(1,n):
            if res[i-1] + limit >= res[i]:
                q_list[-1].append(res[i])
                hmap[res[i]] = group
            else:
                q_list.append(deque([res[i]]))
                group += 1
                hmap[res[i]] = group

        for i in range(n):
            res[i] = q_list[hmap[nums[i]]].popleft()

        return res