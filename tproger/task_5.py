dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
c = 0
for i in sorted(dict, key=dict.get, reverse=True):
    print (i, ':', dict[i])
    c=c+1
    if c == 3:
        break

from heapq import nlargest
result = nlargest(3, dict, key=dict.get)

print()
for i in result:
    print (i, ':' , dict[i])


print(int('ABC', 16))
