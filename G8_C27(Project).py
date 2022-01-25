shirt = ""
trouser = ""

day = input("Enter whether it is a Special(S/s) or Normal(N/n) day: ")

def Dressing(shirt = "White", trouser = "White"):
    return shirt, trouser
    
if  day == "S" or day == "s":
    shirt, trouser = Dressing("Black", "Black")
else:
    shirt, trouser = Dressing()

print("Wear a", shirt, "shirt and a", trouser, "trouser")
