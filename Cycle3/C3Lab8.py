def find_longest_word(ls):
    length = []
    for i in ls:
        length.append((len(i)))
    length.sort()
    return length[-1]
result = find_longest_word(["Apple", "Education", "Grape"])
print("length of longest word: ",result)
