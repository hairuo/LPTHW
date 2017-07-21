import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function and call it with the parameters self and @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# check for certain command argument
if len(sys.argv) == 2 and sys.argv[1] == "english":
    # sys.arg is list, with script's filename as first/0th element but is only created if command argument is given at all
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # fills empty word list with words from downloaded file
    WORDS.append(word.strip())
    # strip is function of module 'string'

print (WORDS)
