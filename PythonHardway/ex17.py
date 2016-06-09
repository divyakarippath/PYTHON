from sys import argv

script,from_file,to_file = argv

txt = open(from_file)
indata = txt.read()

txt_nw = open(to_file,"w")
txt_nw.write(indata)

