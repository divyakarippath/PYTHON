from sys import exit
from random import randint

class Game(object):
    def __init__(self,start):
        self.quips=["you suck at this","Your mom would be proud","Such a luster","My puppy is better at this"]
        self.start = start

    def play(self):
        next = self.start
        i=0
        while True:
            print "\n-----------"
            room = getattr(self,next)
            next = room()
            print next
    def princess_lives_here(self):
        uinput = raw_input(">")

        if uinput=='1':
            return "death"
        elif uinput =='2':
            return "death"
        elif uinput =='3':
            return "gold_koi_pond"
        else:
            return "princess_lives_here"

    def death(self):
        print self.quips[randint(0,len(self.quips)-1)]
        print "hello"
        exit(1)



a_game = Game("princess_lives_here")
a_game.play()