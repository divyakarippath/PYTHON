def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)
def test(a,b):
    print "HI"
def arith(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div


age = add(20,7)
height = sub(168,4)
weight = mul(25,2)
IQ = div(100,2)

what = add(age,sub(height,mul(weight,div(IQ,2))))

print "age :",age
print "height :",height
print "weight :",weight
print "IQ :",IQ
print "What :",what
print test(5,10)

p,q,r,s = arith(10,5)
print "sum : %d\nsub : %d\nmul : %d\ndiv : %d"%(p,q,r,s)
