words = ["This", "is", "good", "is"]
freq = {}

for w in words:
    w = w.lower()
    freq[w] = freq.get(w, 0) + 1

print(freq)
