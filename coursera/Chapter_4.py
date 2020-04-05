### functions
##use functions
#example #1
def inc (y):
    y = y + 1
    return (y)

x = int(input())
x = inc(x)
print (x)

#example #2
def greet (lang, name):
    if lang == 'es':
        print('Hola', name)
    elif lang == 'fr':
        print ('Bonjour', name)
    else:
        print ('Hello', name)

l = input('lang: ',)
n = input('Name: ',)
greet(l, n)
