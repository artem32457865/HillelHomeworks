class Buffer:
    def __init__(self):
        self.data = []

    def add(self, a):
        self.data.extend(a)

        while len(self.data) >= 5:
            print(sum(self.data[:5]))
            self.data = self.data[5:]

    def get_current_part(self):
        return self.data


buffer = Buffer()

while True:
    try:
        numbers = list(map(int, input().split()))
        buffer.add(numbers)
        print(buffer.get_current_part())
    except EOFError:
        break