import glob, os
from hashlib import sha256

def _hashfile(filename):
    """Returns a SHA256 hash of the named file.
    """
    with open(filename, "rb") as f:
        data = f.read()
    return sha256(data).hexdigest()    

def _index(directory):
    """Generates an index of hashcodes for WAV files in a directory.

    Args:
        directory (String): Name of the directory to index
        
    Returns: 
        {String}: Set of hashcodes for the WAV files in the top level of the directory 
    """
    filenames = glob.glob(os.path.join(directory,'*.wav'))
    
    hashcodes = set()
    for fn in filenames:
        hashcodes.add(_hashfile(fn))
    return hashcodes

def _index_filename(directory):
    return os.path.join(directory,'index.txt')

def write_index(directory):
    hashcodes = _index(directory)
    with open(_index_filename(directory), 'w') as f:
        f.write('\n'.join(hashcodes)) 

def read_index(directory):
    with open(_index_filename(directory),'r') as f:
        data = f.read()
    return data.split()

def search_index(filename, directory):
    return _hashfile(filename) in read_index(directory)