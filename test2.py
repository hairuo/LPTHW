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
        "From *** get the *** function, and call it with the parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    # sys.arg is list, with script's filename as first/0th element
    # but is only created if command argument is given at all
    PHRASE_FIRST = True
# sys.argv is a list in Python, which contains the command-line arguments
# passed to the script.
# With the len(sys.argv) function you can count the number of arguments.

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # fills empty word list with words from downloaded file
    WORDS.append(word.strip())
    # strip is to delete return and space

snippets = PHRASES.keys()

test = [w.capitalize() for w in
                   random.sample(WORDS, snippets[0].count("%%%"))]
result = test.replace("%%%", word, 1)
print(result)
# convert(keys, values)
