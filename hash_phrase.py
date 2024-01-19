# based on the https://github.com/fpgaminer/hash-phrase
# which was released into the Public Domain by fpgaminer@bitcoin-mining.com



import hashlib
import math
import sys

from argparse import ArgumentParser


def load_dictionary (max_len=0, dictionary_file="sjp-20240115\slowa.txt"):
    with open (dictionary_file, 'r',encoding='utf8') as f:
        dictionary = f.read ().splitlines ()
    return [w for w in dictionary if len(w)<=(len(w) if max_len==0 else max_len)]

def default_hasher (data):
    return hashlib.sha256(data.encode('ascii')).hexdigest()

def hash_phrase (data, num_words=3, max_len=0, dictionary=None, hashfunc=default_hasher):
    if dictionary is None:
        dictionary=load_dictionary(max_len)
    dict_len = len (dictionary)
    entropy_per_word = math.log (dict_len, 2)
    words_entropy=num_words*entropy_per_word

    # Hash the data and convert to a big integer (converts as Big Endian)
    hash = hashfunc (data)    
    hash = int (hash, 16)

    phrase = []

    for i in range (num_words):
        remainder = hash % dict_len
        hash = hash // dict_len                
        phrase.append (dictionary[remainder])    
    return " ".join (phrase).lower().capitalize()

def hash_entropy(num_words, max_len=0, dictionary=None):
    if dictionary is None:
        dictionary=load_dictionary(max_len)
    return int(num_words * math.log (len (dictionary), 2))

if __name__ == "__main__":

    parser = ArgumentParser(
        prog="hash_phrase.py", description="generates human readable (in human words) hash for a string (passwords etc.)"
    )
    # required parameters
    parser.add_argument(
        "-d",
        "-data",
        dest="data",
        type=str,
        help="string to be hashed",
        required=True,
        metavar="<data>",
    )
    #optional parameters
    parser.add_argument(
        "-n",
        "-wordsNumber",
        dest="num_words",
        type=int,
        help="number of hash words (default 3)",
        required=False,
        default = 3,
        metavar="<num_words>"
    )
    parser.add_argument(
        "-l",
        "-maxWordsLength",
        dest="max_len",
        type=int,
        help="maximum length of hash words (reduces strenght). default value - no limits",
        required=False,
        default=0,
        metavar="<max_len>"
    )

    args = parser.parse_args(sys.argv[1:])

    entropy = hash_entropy(args.num_words,args.max_len)
    if entropy < 28:
        strength = 'very weak'
    elif entropy < 36:
        strength = 'weak - use for local logging only'
    elif entropy < 60:
        strength = 'reasonable - for work, social media'
    elif entropy < 128:
        strength = 'strong - use for banks'
    else:
        strength = 'very strong - usually overkill'
    
    print ("hash :"+hash_phrase (args.data, args.num_words, args.max_len))
    print ("entropy :"+str(entropy))
    print ("strength :"+strength)
