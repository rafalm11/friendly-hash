# friendly-hash

## description

Generates human readable hash for a given string.
Can convert short string to a strong password, for example password with only 3 words has a strength of 64bit hash (with Polish dictionary which contains 3.2mln words), which is considered as a very strong password (stronger than "#;sfżd23*GF)!/ą" !!!!).

Works only with Polish words dictionary as for now


## credits
code is based on https://github.com/fpgaminer/hash-phrase
which was released into the Public Domain by fpgaminer@bitcoin-mining.com

Słownik SJP.PL - wersja do gier słownych
Słownik udostępniany na licencjach GPL 2 oraz
Creative Commons Attribution 4.0 International
https://sjp.pl


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
```hash :Odkłamane pohańbiaj załagodzeniom
entropy :64 ```

sample call:
```python ./hash_phrase.py -d 'password' -n 3 -l 7```
output:
```hash :Pałowań siknęło rolo
entropy :53 ```

sample call:
```python ./hash_phrase.py -d 'password1' -n 3 -l 7```
output:
```hash :Nakopią zezna łkasz
entropy :53 ```