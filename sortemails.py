#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
#To do this look for lines that start with “From”, then look for the third word and keep a running count
#of each of the days of the week. At the end of the program
#print out the contents of your dictionary (order does not matter).

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
	words = list(line.split())
	if not line.startswith("From "):
		continue
	emails = words[2]
	#for word in word
	counts[emails] = counts.get(emails,0) + 1

print(counts)
