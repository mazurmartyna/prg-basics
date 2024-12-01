paragraph = "cat dog mouse cat rat cat mouse"

paragraph = paragraph.split()

paragraphfinal = set(paragraph) | set(paragraph)


total = 0 

for char in paragraphfinal:
    for word in paragraph:
        if char == word:
            total += 1
    if total == 1:
        print(f"{char} appears {total} time in the paragraph")
    else:
        print(f"{char} appears {total} times in the paragraph")
    total = 0