from sys import argv
script,file_name = argv

def print_all(txt):
    print txt.read()
def rewind(txt):
    txt.seek(0)
def print_line(txt):
    print txt.readline()

txt = open(file_name)
print_all(txt)
rewind(txt)

print_line(txt)
print_line(txt)
print_line(txt)

