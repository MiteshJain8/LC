class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.first = defaultdict(set)
        self.second = defaultdict(set)
        for i,num in enumerate(nums2):
            self.second[num].add(i)

    def add(self, index: int, val: int) -> None:
        initial = self.nums2[index]
        self.second[initial].remove(index)
        self.second[initial + val].add(index)
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            ele = tot - num
            if self.second[ele]:
                res += len(self.second[ele])

        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)