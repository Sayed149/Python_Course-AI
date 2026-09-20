def vim_search(text, word):
    matches = []
    start = 0

    while True:
        pos = text.find(word, start)

        if pos == -1:
            break

        matches.append(pos)
        start = pos + 1

    return matches



word = "search"

result = vim_search(text, word)

print("Search word:", word)
print("Positions:", result)

if result:
    print("First match:", result[0])
    print("Next match:", result[1] if len(result) > 1 else "No more matches")
else:
    print("Word not found")