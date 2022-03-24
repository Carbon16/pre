#https://github.com/Carbon16/pre/blob/main/python/task3.py


#Imports
#import json
from datetime import date

#Declaring
member = {}
spons = {}
newMem = True
fName = 0
count = 1
c0 = 1
Valid = False
Valid0 = False
sName = 0
vol = 0
loc = 0
paid = False
nUse = False
today = date.today()
d1 = today.strftime("%d/%m")
y1 = int(today.strftime("%y"))
y2 = y1 + 1
go = True
dosh = 0
k = []
v = []

def add(count):
    newMem = True
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
        member["A" + str(count)]["Date"] = d1
        member["A" + str(count)]["Expiry"] = y2
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
            paid = input("Has user paid the fee? (y/n):")
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
                return count

            if nUse == "n":
                newMem = False
                count = count + 1
                Valid1 = True
                print("Goodbye")
                return count
            else:
                print("Please enter only y or n")
    return member

def get(member):
    #Local init
    get = True
    Valid = False
    #Begin Loop
    while get == True:
        while Valid == False :
            getMen = int(input("What do you want to search? \n1. Voulenteers\n2. Expired\n3. Not paid\nSelect:"))
            if getMen == 1:
                getVol = int(input("What do you want to search? \n1. Gate\n2. Shop\n3. Painting\n4. All\nSelect:"))
                if getVol == 1:
                    for i in member:
                        try:
                            if member[i]["Location"] == "Gate":
                                print("Name: " + str(member[i]["Surname"]) + ", " + str(member[i]["Prename"]))
                        except KeyError:
                            print("**End**")
                if getVol == 2:
                    try:
                        for i in member:
                            if member[i]["Location"] == "Shop":
                                print("Name: " + str(member[i]["Surname"]) + ", " + str(member[i]["Prename"]))
                    except KeyError:
                        print("**End**")
                if getVol == 3:
                    try:
                        for i in member:
                            if member[i]["Location"] == "Painting & Decorating":
                                print("Name: " + str(member[i]["Surname"]) + ", " + str(member[i]["Prename"]))
                    except KeyError:
                        print("**End**")
                if getVol == 4:
                    try:
                        for i in member:
                            if member[i]["Volunteer"] == True:
                                print("Name: " + str(member[i]["Surname"]) + ", " + str(member[i]["Prename"]))
                    except KeyError:
                        print("**End**")

                if getMen == 2:
                    try:
                        for i in member:
                            if member[i]["Date"] > d1 and member[i]["Expiry"] > y1:
                                print("Name: " + str(member[i]["Surname"]) + ", " + str(member[i]["Prename"]))
                    except KeyError:
                        print("**End**")
                if getMen == 3:
                    try:
                        for i in member:
                            if member[i]["Paid"] == False:
                                print("Name: " + str(member[i]["Surname"]) + ", " + str(member[i]["Prename"]))
                    except KeyError:
                        print("**End**")

def spon(spons):
    #Local init
    spon = True
    Valid = False
    global c0
    global dosh
    #Begin Loop
    while Valid == False:
        print("PLEASE BE AWARE THAT THIS SPONSORSHIP WILL COST $200")
        nom = input("Please enter your name:")
        msg = input("Please enter the message you would like:")
        print("PLEASE CONFIRM THE FOLLOWING DETAILS ARE CORRECT")
        print("Name:" + nom + " | Message:" + msg)
        yn = str(input("Please confirm (y/n):"))
        if yn == "y":
            spons.update({c0: [str(nom), str(msg)]})
            dosh = dosh + 200
            print("Sponsorship sucess!")
            Valid = True
            c0 = c0 + 1
        if yn == "n":
            print("Please try again")
            Valid = False
    return spons


while go == True:
    menu = int(input('1. Add new member\n2. Get a member\n3. Sponsor\n4. Display sponsors & money raised\n5. EXIT\nSELECT: '))
    if menu == 1:
        add(count)
    if menu == 2:
        get(member)
    if menu == 3:
        spon(spons)
    if menu == 4:
        print(spons)
        print("Money raised: $" + str(dosh))
    if menu == 5:
        go = False
        print("Goodbye!")
