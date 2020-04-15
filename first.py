x = None
print (x is 1)
print (2 > 1)
def greet():
    return "hello"

print (greet(), "test")
print (greet(), "test123")

def inc(y):
    y = y + 1
    return y
x = 1
print (x)
x = inc (x)
print (x)
x = inc (x)
print (x)
x = inc (x)
print (x)
x = inc (x)
print (x)

def test():
    print ('test')

test()
print ('###############')
print (test())
