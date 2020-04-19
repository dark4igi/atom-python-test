##Lists
x = ['123', ['1', 'dsa'], 123, True, 23.65]
print (x)
print (type(x))
print (len(x))
print(dir(x))
print ()
for y in x:
    print (y)
    print (type(y))
    try:
        print (len(y))
    except:
        print ('variable without len')
    print()

# list mutable
print ()
z = [1, 2, 3, 4, 5]
print (z)
z[2] = 9
print (z)
print()

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print (c)
print (max(c))
print(min(c))
print(sum(c))
print(sum(c) / len (c))
print ()

d = list()
print (d)
d.append('book')
d.append(99)
print (d)
d.append(32.53)
print(d)

print( 99 in d)
print ('dsa' in d)
print ()

e = 'hello world and python'
print (e)
print (type(e))
f = e.split()
print (f)
print (type(f))

for i in f:
    print(i)
g = 'asda-dfsf-fds'
h = g.split('-')
print(g)
print(h)
print(h[1])
print (range(5))
