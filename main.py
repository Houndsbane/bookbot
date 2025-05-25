from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        content_string = f.read()
    return content_string

def main():
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # book_string = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
    # print(count_characters(get_book_text("books/frankenstein.txt")))
    report = sort_dict(count_characters(get_book_text(sys.argv[1])))
    for value in report:
        if value["char"].isalpha():
            print(f"{value['char']}: {value['count']}")
main()