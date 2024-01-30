import sys
from wavtool import search_index

if __name__ == "__main__":
    directory = sys.argv[1]
    filenames = sys.argv[2:]
    for fn in filenames:
        if search_index(fn, directory):
            print(f"{fn} found")
    