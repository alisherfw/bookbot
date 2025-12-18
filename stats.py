def count_words(text):
	count_of_words = len(text.split())
	return count_of_words

def count_characters(text):
    lowercase_text = text.lower()
    count_of_characters = {}
    for i in lowercase_text:
        if i not in count_of_characters:
            count_of_characters[i] = 1
        else:
            count_of_characters[i] = count_of_characters[i] + 1
    return count_of_characters

def sort_on(item):
    return item["num"]

def get_sorted_report(dict):
    char_list = []
    for ch in dict:
        if ch.isalpha():
            char_list.append({"char": ch, "num": dict[ch]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list