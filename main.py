import sys
from stats import get_num_symblos, get_num_words


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def print_report(path, num_words, dict):
    print('============ BOOKBOT ============')
    print('Analyzing book found at ' + path + '...')
    print('----------- Word Count ----------')
    print('Found ' + str(num_words) + ' total words')
    print('--------- Character Count -------')
    items_dict = dict.items()
    for item in items_dict:
        print(item[0] + ": " + str(item[1]))
    print('============= END ===============')


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    file = get_book_text(path)
    dict = get_num_symblos(file)
    words = get_num_words(file)
    print_report(path, words, dict)


if __name__ == "__main__":
    main()
