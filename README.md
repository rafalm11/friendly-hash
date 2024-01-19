# friendly-hash

## description

Generates human readable hash for a given string.
It hashes isput with sha-256 and then transaltes it to human words.
Can convert short string to a strong password, for example password with only 3 words has a strength of 64bit hash (with Polish dictionary which contains 3.2mln words), which is considered as a very strong password (**stronger than "#;sfżd23*GF)!/ą" !!!!**).
It uses sha256 hashing.

Works only with Polish words dictionary as for now

### use cases

possible use cases

* strong and easy to remember password generator

  You do not have to trade security for convenience. You can have many passwords both easy to remember and strong.
  Even if you forget those this passwords - you can always recover them again.
  
  For example you convert:
  
  ```facebook-<something personal>``` into ```Rozbyczać niezasmażenia kijowa``` (strength 64 bytes)
  
  ```gmail-<something personal>``` into ```Niezapłaceniach hangarowych obumierajcież``` (strength 64 bytes)
  
  even if you forget both passwords - the only thing you need to remeber is <something personal> to recover them both


* convert guids to something readable in your application

    for example in your log file it is easier to visually scan for words

* use words instead of numeric codes for inventory identification

    it is easier to repeat words instead of long numbers (especially over the phone)


## use synatax
```
usage: hash_phrase.py [-h] -d <data> [-n <num_words>] [-l <max_len>]

generates human readable (in human words) hash for a string (passwords etc.)

optional arguments:
  -h, --help            show this help message and exit
  -d <data>, -data <data>
                        string to be hashed
  -n <num_words>, -wordsNumber <num_words>
                        number of hash words (default 3)
  -l <max_len>, -maxWordsLength <max_len>
                        maximum length of hash words (reduces strenght).
                        default value - no limits
```                        

## use examples
sample call:
```python ./hash_phrase.py -d 'password' ```
output:
```
hash :Odkłamane pohańbiaj załagodzeniom
entropy :64
strength :strong - use for banks
```

sample call:
```python ./hash_phrase.py -d 'password' -n 3 -l 7```
output:
```
hash :Pałowań siknęło rolo
entropy :53
strength :reasonable - for work, social media
```

sample call:
```python ./hash_phrase.py -d 'password1' -n 3 -l 7```
output (please note the small password change generates completely different hash):
```
hash :Nakopią zezna łkasz
entropy :53
strength :reasonable - for work, social media
```

## credits
code is based on https://github.com/fpgaminer/hash-phrase
which was released into the Public Domain by fpgaminer@bitcoin-mining.com

Słownik SJP.PL - wersja do gier słownych
Słownik udostępniany na licencjach GPL 2 oraz
Creative Commons Attribution 4.0 International
https://sjp.pl