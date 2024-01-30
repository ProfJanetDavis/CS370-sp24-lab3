import sys, glob
from hashlib import sha256

def index(directory):
    """Generates an index of hashcodes for WAV files in a directory.

    Args:
        directory (String): Name of the directory to search
        
    Returns: 
        {String}: Set of hashcodes for the WAV files in the top level of the directory 
    """
    filenames = glob.glob(directory+'/*.wav')
    
    hashcodes = set()
    for fn in filenames:
        data = open(fn, "rb").read()
        hashcodes.add(sha256(data).hexdigest())
    return hashcodes

if __name__ == "__main__":
    directory = sys.argv[1]
    print(index(directory))