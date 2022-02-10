ftot = 0
count = 0
while True:
    print ("This will give you a sum an avarega and a count of entered numbers", "\nWrite done when ready","\nEnter a number:")
    num = input()
    if (num == "done"):
        break
    try:
        fnum = float(num)
    except:
        print("Please enter a number")
    ftot = ftot + fnum
    count = count + 1
if count > 0:
    avg = ftot/count
else:
    avg = 0
print("Total:", ftot, "\nAvarage:", avg, "\nCount:", count)
