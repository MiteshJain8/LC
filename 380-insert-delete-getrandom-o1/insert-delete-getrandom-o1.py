class RandomizedSet:

    def __init__(self):
        self.hset = set()

    def insert(self, val: int) -> bool:
        if val in self.hset:
            return False
        self.hset.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hset:
            return False
        self.hset.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.hset))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()