# regen
The Regular Expression Generator. Give a regex sequence, and get a randomly generated listing of strings that match the sequence.

## Examples
### Help
```
root@kali ~/P/regen# ./regen.py --help
usage: regen [-h] [-v] [-q] [-n NUM] [-l LENGTH] [-t TEST] regex

Regular Expression Generator

positional arguments:
  regex                 regex sequence

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -q, --quiet           surpress extra output
  -n NUM, --num NUM     number to generate
  -l LENGTH, --length LENGTH
                        a probable maximum length
  -t TEST, --test TEST  a known matching test string to confirm regex

Written by TheTwitchy. Source available at gitlab.com/TheTwitchy/regen
```
### Base Run
```
root@kali ~/P/regen# ./regen.py "^[a-z]*\$"
  _ __ ___  __ _  ___ _ __  
 | '__/ _ \/ _` |/ _ \ '_ \
 | | |  __/ (_| |  __/ | | |
 |_|  \___|\__, |\___|_| |_|
            __/ |           
           |___/            
              version 0.1

regen: info: The regular expression validated successfully.
e
o
ff
nj
gx
q
eai
y
z
y
regen: info: Performed 676 tests.
```
### Complex Run
```
root@kali ~/P/regen# ./regen.py -n 5 -l 10 -t 'abc' '^[a-z]{1,4}$'
  _ __ ___  __ _  ___ _ __  
 | '__/ _ \/ _` |/ _ \ '_ \
 | | |  __/ (_| |  __/ | | |
 |_|  \___|\__, |\___|_| |_|
            __/ |           
           |___/            
              version 0.1

regen: info: The regular expression validated successfully.
hv
fi
ssv
ryy
fr
regen: info: Performed 81 tests.
```

## Tips
  * Give a maximum length to help speed up the time to generate strings, if known.
  * Don't forget start-of-line (`^`) and end-of-line (`$`) metacharacters, if relevant. Results may be strange (but valid) otherwise.
