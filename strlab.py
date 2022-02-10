str = ("this is\t/t a piece\t of    /t \tstring.")
print(str)
# puts cap on first letter
cap = str.capitalize()
print(cap)
lenght = len(str)
print (lenght)
if(str.endswith("ng."[lenght-3:])):
    print("Yip Yip")
print(str.expandtabs(10))
print(str.find("e"))
print(str.replace("i","a"))
