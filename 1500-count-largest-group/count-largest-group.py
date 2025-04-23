class Solution:
    def countLargestGroup(self, n: int) -> int:
        lengths = defaultdict(int)
        max_length = count = 0
        for i in range(1, n+1):
            digit_sum = 0
            while i:
                digit_sum += i % 10
                i //= 10
            lengths[digit_sum] += 1
            if lengths[digit_sum] == max_length:
                count += 1
            elif lengths[digit_sum] > max_length:
                max_length += 1
                count = 1
        return count