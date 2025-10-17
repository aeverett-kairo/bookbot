from stats import word_count
from stats import character_count
from stats import sort_characters_by_count
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_books = sys.argv[1]
    book_text = get_book_text(path_to_books)
    total_words = word_count(book_text)
    characters_count = character_count(book_text.lower())
    sorted_characters = sort_characters_by_count(characters_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_books}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["char"] in [" ", "\n"]:
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()