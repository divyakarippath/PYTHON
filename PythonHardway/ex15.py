from sys import argv

script,filename = argv
txtname = open(filename)
print txtname.read()

fname = raw_input("Enter the filename : ")
txt = open(fname)
data = txt.read()
print data