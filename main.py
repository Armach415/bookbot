from stats import word_count, char_count
import sys

if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    #filepath = "books/frankenstein.txt"
    filepath = sys.argv[1]

    report_header = f"============ BOOKBOT ============\n Analyzing book found at {filepath}..."
    report_word_count = f"\n----------- Word Count ---------\nFound {word_count(filepath)} total words"
    report_char_count = f"\n--------- Character Count -------"
    report_end = "\n============= END ==============="
    

    print(report_header + report_word_count + report_char_count + char_count(filepath) + report_end) 


main()
