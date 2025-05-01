class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def is_possible(num):
            remaining_pills = pills
            wsl = SortedList(workers[:num])
            for i in range(num-1, -1, -1):
                if wsl[-1] >= tasks[i]:
                    wsl.pop()
                elif remaining_pills == 0:
                    return False
                else:
                    idx = wsl.bisect_left(tasks[i] - strength)
                    if idx == len(wsl):
                        return False
                    remaining_pills -= 1
                    wsl.pop(idx)
            return True
        
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort(reverse=True)
        res, l, r = 0, 1, min(n, m)
        while l <= r:
            mid = (r-l)//2 + l
            if is_possible(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res 