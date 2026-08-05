n = int(input())

s = f"{n:04d}"

if len(set(s)) == 4:
    print(True)
else:
    print(False)