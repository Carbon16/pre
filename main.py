#Declaring
member = {}
newMem = True
fName = 0
count = 0
Valid = False
Valid0 = False
sName = 0
vol = 0
loc = 0
paid = False
nUse = False

#Loops while there is a new member to add
while newMem == True:
    member[count] = {}
    #Local init
    Valid = False
    Valid0 = False
    Valid1 = False
    #Entering names
    print("Please enter your first name:")
    input(fName)
    print("Please enter your surname:")
    input(sName)
    # Validate
    while len(str(fName)) == 0 or len(str(sName)) == 0:
        print("Please enter your name")
        print("Please enter your first name:")
        input(fName)
        print("Please enter your surname:")
        input(sName)
    
    #Stores the name in the nested dictionary
    member[count]["Prename"] = fName
    member[count]["Surname"] = sName
    ##member[count]["Join Date"] = CURRENT_DATE
    #Volunteering
    print(" you wish to volunteer? (y/n):")
    input(vol)
    #Choose location
    if vol == "y": 
        while Valid == False :
            print("Where do you want to volunteer? \n1. Shop\n2. Gate\n3. Painting & Decorating")
            input(loc)
            if loc == 1:
                member[count]["Volunteer"] = True
                member[count]["Location"] = "Shop"
                Valid = True
            if loc == 2:
                member[count]["Volunteer"] = True
                member[count]["Location"] = "Gate"
                Valid = True
            if loc == 3:
                member[count]["Volunteer"] = True
                member[count]["Location"] = "Painting & Decorating"
                Valid = True
            #Validate
            else:
                print("Please select an option")
                Valid = False

    #Validation and paycheck
    while Valid0 == False:
        print("Has user paid the fee? (y/n)")
        input(paid)
        if paid == "y": 
            member[count]["Paid"] = True
            Valid0 = True
        if paid == "n":
            member[count]["Paid"] = False
            Valid0 = True
        else:
            print("Please enter only y or n")
            Valid0 = False

    while Valid1 == False:
        print("Add new member? (y/n):")
        input(nUse)
        if nUse == "y":
            newMem = True
            Valid1 = True
        if nUse == "n":
            newMem = False
            Valid1 = True
            print("Goodbye")
        else:
            print("Please enter only y or n")
        
    

