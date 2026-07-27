def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Start!"


for item in countdown(5):
    print(item)