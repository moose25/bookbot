# main.py

import sys
from stats import get_num_words, get_char_count, sort_char_counts


def get_book_text(filepath: str) -> str:
    """Return the entire contents of the file at `filepath` as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = get_char_count(text)
    sorted_chars = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
