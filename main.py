import sys
from stats import get_book_text, count_words, count_characters, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        book_content = get_book_text(book_path)
        num_words = count_words(book_content)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        char_counts = count_characters(book_content)
        sorted_chars = sort_char_counts(char_counts)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    except FileNotFoundError:
        print("Error: File not found at {book_path}. Please check the filepath.")

if __name__ == "__main__":
    main()
