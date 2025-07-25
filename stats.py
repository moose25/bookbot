# stats.py

def get_num_words(text: str) -> int:
    """Return the number of words in the given text."""
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict:
    """Return a dictionary with the count of each character (case-insensitive)."""
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_char_counts(char_dict: dict) -> list:
    """
    Return a list of dictionaries, each with keys 'char' and 'num',
    sorted from highest to lowest count.
    """
    sorted_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list
