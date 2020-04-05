s = int(input())
print (s)
d = s // (24*3600)
s = s % (24*3600)
h = s // 3600
s = s % 3600
m = s // 60
s = s % 60
print ('days :', d)
print ('hours:', h)
print ('minutes:', m)
print ('seconds :', s)
