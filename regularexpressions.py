import re
name = input("Enter file name to sumarise numbers in text")
fh = open(name)
sumval = 0
for line in fh:
    if not re.findall('[0-9]+', line):
        continue
    value = re.findall('[0-9]+', line)
    allvalues.append(values)
    value_map = map(int, value)
    integer_list = list(value_map)
    sumval = sumval + sum(integer_list)
    print(integer_list)
    print(sumval)
