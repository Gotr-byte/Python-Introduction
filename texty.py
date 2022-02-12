#Write a program that reads the words in words.txt and stores them as keys in a dictionary.
#It doesn’t matter what the values are. Then you can use the in operator as a fast way
#to check whether a string is in the dictionary.

name = input("Enter file:")

if len(name) < 1:
    name = "text.txt"
handle = open(name)
counts = dict()

for line in handle:
	words = list(line.split())
	for word in words:
	   counts[word] = counts.get(word,0) + 1

print(counts)
key = input ("Enter key: ")
if key in counts:
    x = counts[key]
    print ("The key", key, "opens value", x)
else :
    x = 0
    print ("Key not in counts")
