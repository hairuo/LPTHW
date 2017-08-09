class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, number, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.number = number[1]
        self.object = object[1]

    def to_tuple(self):
        return (self.subject, self.verb, self.number, self.object)


# Peek word in list and return type of word:
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# Confirm the type of word and pop it:
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# Skip words we don't care: scream at the bear->scream bear
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

# based functions above, analysis verb and skip 'stop':
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_number(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'number':
        return match(word_list, 'number')
    else:
        return ('number', 1)

# sentence instead of word as above:
def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    elif next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    number = parse_number(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, number, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)
