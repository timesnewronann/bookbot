from collections import defaultdict

# Takes text from the book as a string
# Returns the number of words in the string


def word_counter(text):
    words = text.split()
    number_words = len(words)

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
            if letter.isalpha():
                counts[letter] += 1

    # We need to go through each word and count the number of times a letter appears

    # Convert dictionary of characters into a list of dictionaries
    # Use .sort() to sort the number of occurences
    # I used a default dict so I used dict and sorted
    # We only care about alpha numeric characters
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


def main():
    path = "books/frankenstein.txt"
    print(f"--- Begin report of {path} ---")
    with open(path) as f:
        file_contents = f.read()
        # print(file_contents)

        print(f"{word_counter(file_contents)} words found in the document")

        sorted_counts = character_counter(file_contents)

        # go through the dictionary
        for letter, count in sorted_counts:
            print(f"The '{letter}' was found {count} times")
    print("--- End report ---")


main()
