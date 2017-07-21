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

# convert(keys, values)
def convert(snippet, phrase):
    # initialise lists with items to be compiled into sentence later
    # list comprehension is way to construct lists from conditional statements
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    #random.sample means select snippet.count words by random.
    #snippet.count calculate and display how many times "%%%" appears in snippet.
    other_names = random.sample(WORDS, snippet.count("***"))
    # 'sample(population, k)' is method of class 'random' that returns list of
    # k elements picked randomly from population
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        # random.randint(a, b) return a random integer N such that a <= N <= b.
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        # for example, str = '-', seq = ("a", "b", "c"), so that str.join(seq) == a-b-c
        # hence here it use ',' to separate words.

    for sentence in snippet, phrase:
        result = sentence[:]
        # CSQ: "slice" syntax of copying a list from 1st to last element
        # next 3 for loops insert elements from _names lists into result sentence

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result) #result->results

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys() # key->keys
        # .keys() means all keys is retrieved.
        random.shuffle(snippets)
        # .shuffle means shuffling a list of objects


        for snippet in snippets:
            phrase = PHRASES[snippet]   # phrase means values while snippets are keys
            question, answer = convert(snippet, phrase) # convert(keys, values)
            if PHRASE_FIRST:
                question, answer = answer, question
            # poses assembled question, waits for input & displays answer no matter what
            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    # class in module 'exceptions'; is returned when Python tries to read beyond end of file
    print "\nBye"
