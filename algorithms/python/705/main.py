class MyHashSet:
    def __init__(self):
        self.capacity = int(10 ** 4 + 1)
        self.numItems = 0
        self.table = [None] * self.capacity

    def hash(self, key: str):
        P = 11667697
        x = 62057
        v = 0
        for i in range(len(key) - 1, -1, -1):
            v = (v * x + ord(key[i])) % P
        return self.hashInteger(v)

    def hashInteger(self, x: int):
        P = 4210098769
        a = 42283
        b = 44267
        v = (a * x + b) % P
        return v % self.capacity

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = self.hashInteger(key)
        if self.table[index]:
            self.table[index].append(key)
        else:
            self.table[index] = [key]
        self.numItems += 1

    def remove(self, key: int) -> None:
        index = self.hashInteger(key)
        found = -1
        if self.contains(key):
            for i, k in enumerate(self.table[index]):
                if k == key:
                    found = i
                    break
            if found != -1:
                self.table[index][found] = self.table[index][-1]
                self.table[index].pop()
                self.numItems -= 1

    def contains(self, key: int) -> bool:
        index = self.hashInteger(key)
        if self.table[index]:
            return key in self.table[index]
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)