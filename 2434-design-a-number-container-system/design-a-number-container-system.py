class NumberContainers:

    def __init__(self):
        self.num_to_idx = defaultdict(SortedList)
        self.idx_to_num = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if self.idx_to_num[index]:
            self.num_to_idx[self.idx_to_num[index]].remove(index)
        self.idx_to_num[index] = number
        self.num_to_idx[number].add(index)

    def find(self, number: int) -> int:
        if self.num_to_idx[number]:
            return self.num_to_idx[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)