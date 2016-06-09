def break_words(stuff):
    return stuff.split(' ')
def sort_words(stuff):
    return sorted(stuff)
print break_words("HI WELCOME")
print sort_words(break_words("Me And My Friends"))

print break_words("Me And My Friends").pop(0)
print break_words("Me And My Friends").pop(-1)