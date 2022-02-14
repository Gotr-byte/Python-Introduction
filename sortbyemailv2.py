#Exercise 1: Revise a previous program as follows: Read and parse the “From”
#lines and pull out the addresses from the line.
#Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person
#who has the most commits.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
rcount = dict()
for line in handle:
    words = list(line.split())
    if not line.startswith("From") or line.startswith("from"):
        continue
    emails = words[1]
    counts[emails] = counts.get(emails, 0) + 1
tmp = list()
for k, v in counts.items() :
    tmp.append( (v, k) )
print(sorted(tmp, reverse = True))
