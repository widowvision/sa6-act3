strings = ["apple", "banana", "orange", "kiwi", "grape"]
sorted_strings = sorted(strings, key=lambda s: (len(s), s))
print(sorted_strings)
