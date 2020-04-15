### Data type

##file


# example open file
xfile = open (file.txt)
for line in xfile:
    print (line )
## work with strings
#
line.rstrip() # strip whitespaces and newline from the right-hand of the string
line.startswith('some text') # became true if line starts with 'some text'
line.upper() # upper case for line
line.lower() # lower case for line
line[20:] # string after 20 chapter
line[:20] # string before 20 chapter
line [3:8] # string from 3rd to 8th, not include 8th
