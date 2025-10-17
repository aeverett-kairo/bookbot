from stats import word_count
from stats import character_count
from stats import sort_characters_by_count
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    #book_text = get_book_text("/home/aarone/github.com/bookbot/books/frankenstein.txt")
    total_words = word_count(book_text)
    characters_count = character_count(book_text.lower())
    sorted_characters = sort_characters_by_count(characters_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["char"] in [" ", "\n"]:
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    print(sys.arg)


if __name__ == "__main__":
    main()