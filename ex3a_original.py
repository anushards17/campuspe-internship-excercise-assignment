sentence = input("Enter a sentence: ")

print("Original:", sentence)
print("Characters (with spaces):", len(sentence))
print("Characters (without spaces):", len(sentence.replace(" ", "")))

words = sentence.split()
print("Total words:", len(words))
print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("Title Case:", sentence.title())

if len(words) > 0:
    print("First word:", words[0])
    print("Last word:", words[-1])

print("Reversed:", sentence[::-1])