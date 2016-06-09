def print_none():
    print "none"
def print_one(arg1):
    print arg1
def print_two(arg1,arg2):
    print arg1,
    print arg2
def print_two_new(*args):
    arg1,arg2=args
    print arg1,
    print arg2
print_none()
print_one("ZERO")
print_two("ONE","TWO")
print_two_new("THREE","FOUR")