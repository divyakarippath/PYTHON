formatter = "%r %r %r %r"
print formatter
print formatter %(1,2,3,4)
print formatter %("One","Two","Three","Four")
print formatter %(formatter,formatter,formatter,formatter)
print formatter %("A","B","C","D")
