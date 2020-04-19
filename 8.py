fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    list1 = line.split()
    print (list1)
    for word in list1 :
        if word not in  lst :
            lst.append(word)
lst.sort()
print (lst)
