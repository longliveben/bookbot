def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_char_counts(char_count_dict):
    # Convert dictionary to list of dictionaries, only for alphabetical chars
    char_list = [{"char": char, "num": count} for char, count in char_count_dict.items() if char.isalpha()]
    # Sort by num in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
