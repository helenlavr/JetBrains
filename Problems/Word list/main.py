text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

'''
length = int(input())
word_list = []
for sentence in text:
        for word in sentence:
                if len(word) <= length:
                        word_list.append(word)
print(word_list)
'''
length = int(input())
print([word for sentence in text for word in sentence if len(word) <= length])
