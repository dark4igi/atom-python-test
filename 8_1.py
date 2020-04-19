fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    list1 = line.rstrip()
    print (list1)
