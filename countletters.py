import string
file = input("Enter file name:")
fh = open(file)
counts = dict()
totallet = 0
for line in fh:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', ' '))
    line = line.translate(str.maketrans('', '', '\n'))
    line = line.lower()
    letters = tuple(line)
    for letter in letters:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
        totallet = totallet + 1
tmp = list()
for k, v in counts.items() :
    v = int(v / totallet * 100)
    tmp.append( (k, v) )
print(sorted(tmp, reverse = False))
print(totallet)
