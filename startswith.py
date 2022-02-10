fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "startswith.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    count = count + 1
    words = line.split()
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
