#Imports
import json
from datetime import date

#Declaring
member = {}
newMem = True
fName = 0
count = 1
Valid = False
Valid0 = False
sName = 0
vol = 0
loc = 0
paid = False
nUse = False
today = date.today()
d1 = today.strftime("%d/%m/%Y")

#Loops while there is a new member to add
while newMem == True:
    member["A" + str(count)] = {}
    #Local init
    Valid = False
    Valid0 = False
    Valid1 = False
    #Entering names
    fName = input("Please enter your first name:")
    sName = input("Please enter your surname:")
    # Validate
    while len(str(fName)) == 0 or len(str(sName)) == 0:
        print("Please enter your name.")
        fName = input("Please enter your first name:")
        sName = input("Please enter your surname:")
    #Stores the name in the nested dictionary
    member["A" + str(count)]["Prename"] = fName
    member["A" + str(count)]["Surname"] = sName
    member["A" + str(count)]["Join Date"] = d1
    #Volunteering
    vol = input("Do you wish to volunteer? (y/n):")
    #Choose location
    if vol == "y": 
        while Valid == False :
            loc = int(input("Where do you want to volunteer? \n1. Shop\n2. Gate\n3. Painting & Decorating\nSelect:"))
            if loc == 1:
                member["A" + str(count)]["Volunteer"] = True
                member["A" + str(count)]["Location"] = "Shop"
                Valid = True
            if loc == 2:
                member["A" + str(count)]["Volunteer"] = True
                member["A" + str(count)]["Location"] = "Gate"
                Valid = True
            if loc == 3:
                member["A" + str(count)]["Volunteer"] = True
                member["A" + str(count)]["Location"] = "Painting & Decorating"
                Valid = True


    #Validation and paycheck
    while Valid0 == False:
        paid = input("Has user paid the fee? (y/n)")
        if paid == "y": 
            member["A" + str(count)]["Paid"] = True
            Valid0 = True
        if paid == "n":
            member["A" + str(count)]["Paid"] = False
            Valid0 = True

    while Valid1 == False:
        nUse = input("Add new member? (y/n):")
        if nUse == "y":
            newMem = True
            Valid1 = True
            count = count + 1
            
        if nUse == "n":
            newMem = False
            Valid1 = True
            print("Goodbye")
        else:
            print("Please enter only y or n")


#Exporting/importing the dict as json

f = open("save.json", "w")
f.write(json.dumps(member))
f.close()
with open('save.json') as json_file:
    data = json.load(json_file)