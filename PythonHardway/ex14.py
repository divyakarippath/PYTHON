from sys import argv

script,username = argv
prompt = '>'

print "Hi %s , I am the %s script"%(username,script)
print "whats ur age %s?"%username
age = raw_input(prompt)
print "You entered %r"%age