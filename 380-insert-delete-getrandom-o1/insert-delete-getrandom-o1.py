class RandomizedSet:

    def __init__(self):
        import random
        self.s = set()

    def insert(self, val: int) -> bool:
        b = False
        if val not in self.s:
            b = True
            self.s.add(val)
        return b

    def remove(self, val: int) -> bool:
        b = False
        if val in self.s:
            self.s.remove(val)
            b = True
        return b

    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()