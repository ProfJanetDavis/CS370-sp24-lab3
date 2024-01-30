import sys
from wavtool import index, index_filename

if __name__ == "__main__":
    directory = sys.argv[1]
    hashcodes = index(directory)
    indexfilename = index_filename(directory)
    with open(indexfilename, 'w') as f:
        f.write('\n'.join(hashcodes)) 