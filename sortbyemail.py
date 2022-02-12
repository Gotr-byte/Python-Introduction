#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary
#to count how many messages have come from each email address, and print the dictionary.
#Exercise 5: This program records the domain name (instead of the address) where the message
#was sent from instead of who the mail came from (i.e., the whole email address).
#At the end of the program, print out the contents of your dictionary.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    words = list(line.split())
    if not line.startswith("From") or line.startswith("from"):
        continue
    emails = words[1]
    #print(emails)
    x = emails.find("@")
    print(x)
    domains = emails[x:]
	#for word in word
    counts[domains] = counts.get(domains,0) + 1

print(counts)

#Exercise 4: Add code to the above program to figure out who has the most messages in the file.
#After all the data has been read and the dictionary has been created,
#look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
#to find who has the most messages and print how many messages the person has.

largest = None
print('Before:', largest)
for itervar in counts:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Most frequent:', largest, counts[largest])

#Exercise 5: This program records the domain name (instead of the address) where the message
#was sent from instead of who the mail came from (i.e., the whole email address).
#At the end of the program, print out the contents of your dictionary.
