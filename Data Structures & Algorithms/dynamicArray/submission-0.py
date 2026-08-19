class DynamicArray:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self._size = 0
        self._capacity = capacity
        self._array = [None] * capacity

    def _check_index(self, index: int):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")

    def get(self, i: int) -> int:
        self._check_index(i)
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        self._check_index(i)
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._array[self._size] = n
        self._size += 1

    def popback(self) -> int:
        if self._size == 0:
            raise IndexError("Pop from empty array")
        val = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return val

    def resize(self) -> None:
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self._capacity
