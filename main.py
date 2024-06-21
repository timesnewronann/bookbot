from collections import defaultdict

# Takes text from the book as a string
# Returns the number of words in the string


def word_counter(text):
    words = text.split()
    number_words = len(words)
    print(f"Number of words: {number_words}")

    return number_words

# Takes the text from the book as a string
# Returns the number of times each character appears in the string
# Convert any character to lowercase


def character_counter(text):
    # We split the letters by words
    words = text.split()

    counts = defaultdict(int)
    # We can go through the list store each letter count in a dictionary
    for word in words:
        lowercase_word = word.lower()  # lowercased it
        for letter in lowercase_word:
            counts[letter] += 1

    # We need to go through each word and count the number of times a letter appears
    print(counts)
    return counts


def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

        word_counter(file_contents)
        character_counter(file_contents)


main()
