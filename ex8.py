# Should I use %s or %r for formatting?
# You should use %s and only use %r for getting debugging information about something. The %r
# will give you the "raw programmer's" version of variable, also known as the "representation."
# r means "raw" format here.

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
