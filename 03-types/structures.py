text = input("Enter a string: ").strip()
letters = [(letter, text.count(letter)) for letter in set(tuple(text))]
letters.sort(key=lambda x: x[1], reverse=True)

with open('output.txt', 'w') as f:
    f.write(f'Věta: {text}\n')
    f.write('Četnost výskytu písmen:\n-----------------------\n')
    f.write("[")
    for item in letters[:-1]:
        f.write(f"{item},\n")
    f.write(f"{letters[-1]}]")