paragraph = "cat dog mouse cat rat cat mouse"

paragraph = paragraph.split()

paragraphcount = {}

for char in paragraph:
    paragraphcount[char] = 0

for char in paragraph:
    if char in paragraph:
        paragraphcount[char] += 1

print(paragraphcount)