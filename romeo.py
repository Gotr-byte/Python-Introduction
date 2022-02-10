fname = input("Enter file name: ")
fh = open(fname)
lst = list()
i=0
for line in fh:
    sline = list(line.split())
    for i in range(len(sline)) :
        wrd = sline[i]
        if wrd not in lst:
            lst.append(wrd)
lst.sort()
print(lst)
