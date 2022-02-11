#Exercise 1: Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.
tochop = ["Bla","Bli" , "blu", "Arg", 7]
print(tochop)

def chop(tochop):
    ltochop = len(tochop)
    del tochop[0]
    del tochop[ltochop-2]

chop(tochop)
print(tochop)

#The output looks like this:

#['Bla', 'Bli', 'blu', 'Arg', 7]
#['Bli', 'blu', 'Arg']
