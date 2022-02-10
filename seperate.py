str = 'X-DSPAM-Confidence:0.8475'
print(str)
colon = str.find(":")
fnum = float(str[colon+1:])
print("Number from string equals:", fnum)
