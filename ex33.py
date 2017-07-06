# i = 0
# numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the botton is is %d" % i
#
#

#
# for num in numbers:
#     print num

# def create_numbers(i, j, max_numb):
#     # i = 0
#     numbers = []
#     while i < max_numb:
#         print "At the top i is %d" % i
#         numbers.append(i)
#
#         i = i + j
#         print "Numbers now: ", numbers
#         print "At the botton i is %d" % i
#
#     return numbers
#
# print create_numbers(2, 4, 16)

def make_numbers(i, j, max_numb):
    numbers = []
    for i in range(i, max_numb, j):
        print "At the top is is %d" % i
        numbers.append(i)
        # i = i + j
        print "Numbers now: ", numbers
        print "At the botton i is %d" % i

    return numbers
print make_numbers(3, 4, 21)

# print range(1, 6, 2)

