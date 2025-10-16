from stats import word_count
from stats import character_count
from stats import sort_characters_by_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("/home/aarone/github.com/bookbot/books/frankenstein.txt")
    total_words = word_count(book_text)
    characters_count = character_count(book_text.lower())
    sorted_characters = sort_characters_by_count(characters_count)
    print(f"Found {total_words} total words")
    print(characters_count)
    print(sorted_characters)


if __name__ == "__main__":
    main()