class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num:
            self.prefix.append(self.prefix[-1]*num)
        else:
            self.prefix = [1]

    def getProduct(self, k: int) -> int:
        if len(self.prefix) > k:
            return self.prefix[-1]//self.prefix[-1-k]
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)