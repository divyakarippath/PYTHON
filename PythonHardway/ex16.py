from sys import argv
script,filename = argv
txt = open(filename,"w")
txt.truncate()

line1=raw_input("line 1:")
line2=raw_input("line 2:")

txt.write(line1)
txt.write("\n")
txt.write(line2)

txt.close()
