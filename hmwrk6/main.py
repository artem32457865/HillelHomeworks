class CandyStash:
    MAX_CAPACITY = 50

    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Amount must be a non-negative integer")

    def __init__(self, count):
        self.validate_amount(count)
        self._count = min(count, self.MAX_CAPACITY)

    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)

    def __str__(self):
        return f"CandyStash ({self.count}/{self.MAX_CAPACITY})"

    def __repr__(self):
        return f"CandyStash ({self.count}/{self.MAX_CAPACITY})"

    def __add__(self, other):
        self.validate_amount(other)
        return CandyStash(min(self.count + other, self.MAX_CAPACITY))

    def __sub__(self, other):
        self.validate_amount(other)
        return CandyStash(max(self.count - other, 0))

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self.count == other.count
        if isinstance(other, int):
            return self.count == other
        return False



stash = CandyStash(20)
print(stash)               

stash = stash + 40
print(stash)              

stash = stash - 60
print(stash)               

full = CandyStash.full_stash()
print(full)                

print(full == 50)          
print(full == stash)       

stash.count = 70
print(stash)               