print ("Enter hours:")
hours = input()
pay = None
try:
	fhours = float(hours)
except:
	print ("Enter numeric value of hours")
print ("Enter rate:")
rate = input()
try:
	frate = float(rate)
except:
	print ("Enter numeric value of rate")

if fhours > 0 and fhours <= 40:
	pay = frate * fhours
elif fhours > 40:
	pay = 40 * frate + (fhours - 40) * 1.5 * frate
else:
	print("Enter values greater than 0.")

print("Your pay kind Sir is the following:", pay)