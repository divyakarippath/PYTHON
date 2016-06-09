class sample(object):
    def __init__(self):
        self.number = 0
        print "1"
    def some_function(self):
        print "Hello"
    def add_me_up(self,more):
        self.number+=more
        return self.number
a=sample()
b=sample()

a.some_function()
b.some_function()

print a.add_me_up(10)
print a.add_me_up(10)
print b.add_me_up(20)
print b.add_me_up(20)

print a.number
print b.number


