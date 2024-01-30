import sys, glob, os
from hashlib import sha256

def index(directory):
    """Generates an index of hashcodes for WAV files in a directory.

    Args:
        directory (String): Name of the directory to index
        
    Returns: 
        {String}: Set of hashcodes for the WAV files in the top level of the directory 
    """
    filenames = glob.glob(os.path.join(directory,'*.wav'))
    
    hashcodes = set()
    for fn in filenames:
        data = open(fn, "rb").read()
        hashcodes.add(sha256(data).hexdigest())
    return hashcodes

def writeIndex(directory):
    """Writes hashcodes for WAV files in a directory to 
    index.txt in that directory.

    Args:
        directory (String): Name of the directory to index
    """
    hashcodes = index(directory)
    indexfilename = os.path.join(directory,'index.txt')
    with open(indexfilename, 'w') as f:
        f.write('\n'.join(hashcodes))

if __name__ == "__main__":
    writeIndex(sys.argv[1])