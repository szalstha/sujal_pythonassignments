words = ["apple", "banana", "apple", "orange", "banana", "banana"]
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

duplicates = {k: v for k, v in freq.items() if v > 1}
print(duplicates)
