def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(words):
    word_list = get_book_text.split()
    count = 0
    for word in word_list:
     count += 1
    return count

def main():
    get_book_text("/home/aarone/github.com/bookbot/books/frankenstein.txt")
    print(f"found {word_count} total words")

if __name__ == "__main__":
    main()