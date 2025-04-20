class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        counted = {}

        for answer in answers:
            if answer in counted and counted[answer] > 0:
                counted[answer] -= 1
            else:
                count += answer + 1
                counted[answer] = answer
        return count