def to_title_case(sentence):
    words = sentence.split()
    return " ".join(w.capitalize() for w in words)

print(to_title_case("hello world from python"))
