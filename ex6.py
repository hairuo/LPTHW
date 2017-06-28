x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

# The %s specifier converts the object using str(), and %r converts it using repr().
# %r shows with quotes:
# https://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
# repr(object): Return a string containing a printable representation of an object.
# https://docs.python.org/2/library/functions.html#repr
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! % r"
# joke_evaluation = "Isn't that joke so funny?! % s"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

