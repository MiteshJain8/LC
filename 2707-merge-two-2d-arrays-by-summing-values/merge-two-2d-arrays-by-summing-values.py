class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hmap = defaultdict(int)
        res = []
        for i,j in nums1:
            hmap[i] = j
        for i,j in nums2:
            hmap[i] += j
        for k,v in sorted(hmap.items()):
            res.append([k,v])
        return res