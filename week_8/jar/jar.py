class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return(self.size * "🍪")

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if 0 > capacity:
            raise ValueError("Capacity of Jar cannot be negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Size cant be larger than capacity")
        if 0 > size:
            raise ValueError("Size cant be a negative number")
        self._size = size

def main():
    jar1 = Jar()
    jar1.deposit(3)
    print(jar1.size)

if __name__ == "__main__":
    main()
