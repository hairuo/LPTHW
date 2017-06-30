print "How old are you?"
# input() seems equal to raw_input() ?
age = input()
print "How tall re you?"
height = raw_input()
print "How much do you weight?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


# What's the difference between input() and raw_input()?
# The input() function will try to convert things you enter as if they were Python code, but it has
# security problems so you should avoid it.

# see more details: difference between Python input and raw_input
# http://www.pythonclub.org/python-basic/input

