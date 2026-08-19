class MyHashSet:

    def __init__(self):
        self.arr = [-1] * 1000001
        

    def add(self, key: int) -> None:
        self.arr[key] = 1
        

    def remove(self, key: int) -> None:
        self.arr[key] = -1
        

    def contains(self, key: int) -> bool:
        if self.arr[key] == 1:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)