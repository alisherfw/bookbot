import sys
from stats import count_words, count_characters, get_sorted_report

def get_book_text(path):
	file_contents = ""
	with open(path) as f: 
		return f.read()

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")

	content = get_book_text(sys.argv[1])

	num_words = count_words(content)
	num_chars = count_characters(content)
	sorted_report = get_sorted_report(num_chars)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	for item in sorted_report:
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

if __name__ == '__main__':
	main()
