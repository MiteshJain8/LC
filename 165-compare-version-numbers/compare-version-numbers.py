class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = list(map(int,version1.split('.')))
        lst2 = list(map(int,version2.split('.')))
        v1 = len(lst1)
        v2 = len(lst2)
        i = j = 0
        while i < v1 and j < v2:
            if lst1[i] < lst2[j]:
                return -1
            elif int(lst1[i]) > lst2[j]:
                return 1
            i += 1
            j += 1
        while i < v1:
            if lst1[i] != 0:
                return 1
            i += 1
        while j < v2:
            if lst2[j] != 0:
                return -1
            j += 1
        return 0