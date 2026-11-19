class MyHashSet:

    def __init__(self):
        self.setBoy = []

        

    def add(self, key: int) -> None:
        if key not in self.setBoy:
            self.setBoy.append(key)

    def remove(self, key: int) -> None:
        if key in self.setBoy:
            self.setBoy.remove(key)

        

    def contains(self, key: int) -> bool:
        return key in self.setBoy

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)