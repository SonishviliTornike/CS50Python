
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("No space available")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError(f"This {n} amount of cookies aren't available")
        self.size = self.size - n
    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Cant be 0 or Negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("No space")
        self._size = size


jar = Jar()

jar.deposit(3)

jar.withdraw(1)

print(jar)

















# class Jar:
#     def __init__(self, capacity=12):
#         if not isinstance(capacity, int) or capacity < 0:
#             raise ValueError("Capacity must be a non-negative integer.")
#         self.capacity = capacity
#         self.size = 0

#     def __str__(self):
#         return "🍪" * self.size

#     def deposit(self, n):
#         if not isinstance(n, int) or n < 0:
#             raise ValueError("Number of cookies must be a non-negative integer.")
#         if self.size + n > self.capacity:
#             raise ValueError("Too many cookies!")
#         self.size += n
#         return self.size

#     def withdraw(self, n):
#         if not isinstance(n, int) or n < 0:
#             raise ValueError("Number of cookies must be a non-negative integer.")
#         if self.size - n < 0:
#             raise ValueError("Not enough cookies!")
#         self.size -= n
#         return self.size

#     @property
#     def capacity(self):
#         return self._capacity

#     @capacity.setter
#     def capacity(self, capacity):

#         self._capacity = capacity

#     @property
#     def size(self):
#         return self._size

#     @size.setter
#     def size(self, size):
#         self._size = size

# def main():
#     jar = Jar()
#     jar.deposit(3)
#     jar.withdraw(1)
#     print(jar.capacity)
#     print(jar.__str__())

# if __name__ == "__main__":
#     main()

