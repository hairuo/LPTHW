from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# script, first, second, third = argv
# ValueError: need more than 1 value to unpack
# see : https://www.zhihu.com/question/19932406/answer/39822390
# use command: py -2 ex13.py first 2nd 3rd

