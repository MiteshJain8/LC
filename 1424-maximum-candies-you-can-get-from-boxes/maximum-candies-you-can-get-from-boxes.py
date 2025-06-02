class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        dq = deque()
        available_boxes = set()
        remove_boxes = set()
        for u in initialBoxes:
            if status[u]:
                dq.append(u)
            else:
                available_boxes.add(u)
        n = len(status)
        res = 0
        while dq:
            u = dq.popleft()
            res += candies[u]

            for v in keys[u]:
                status[v] = 1
            
            for v in containedBoxes[u]:
                available_boxes.add(v)

            for v in available_boxes:
                if status[v]:
                    dq.append(v)
                    remove_boxes.add(v)

            available_boxes = available_boxes - remove_boxes

        return res       