words = ["apple", "cat", "banana", "sun", "orange", "dog"]

for word in words:
    if (length := len(word)) > 4:
        print(f"{word} - {length}")