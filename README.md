[![Run](https://github.com/Carbon1769/pre/actions/workflows/pylint.yml/badge.svg)](https://github.com/Carbon1769/pre/actions/workflows/pylint.yml)

# pre

This is the repo for the iGCSE pre release. 
The file names should be pretty self explanatory.

## Plan

https://docs.google.com/document/d/1FQm5Npjkg_NUYaEIm6kkYrr9-I93S5KD6s59IcwAkl0/edit

Important numbers:
Members: $75 per year
Can volunteer to help
Can sponsor plank with message  for $200

Need:
Need to calculate initial income
Your program or programs must include appropriate prompts for the entry of data. Data must be
validated on entry.
All outputs, including error messages, need to be set out clearly and understandably.
All variables, constants and other identifiers must have meaningful names.
Functions need to have descriptive names

Data structures:
Fname
Nested dictionary/dictionary of dictionaries, eg:


Array
Example data types
Dictionary (make durable with json export)
Json durable object, export all as a json string and save to a .json file; then check for presence of .json file at start of loop
Data is temporarily stored in dictionary value, then exported and saved as json


Vars:

newMem : var : bool ; Used to control loops | alternatively can be string (y/n)

Member : dict (nested) : mixed type

newMem : var : bool

fName : var : str

count : var : int

Valid : var : bool 

Valid0 : var : bool 

sName : var : str

vol : var : bool : volunteer menu

loc  : var : int : volunteer location menu

paid : var : bool

nUse : var : bool : NEW USER 

today : var : str : date imported from datetime

d1 : var : str : date imported from datetime

get : var : bool

go : var : bool : main while loop



Functions:

Get:

Add:

Programming concepts:

Menu

While loop for new members (newMem):
Prompts for new members
Inputs
Validation {volunteer y/n, bool; volunteer area, pre-def; date of joining, cannot be in future; paid, bool | floatl}

While/for (number of people?)  loop for output (newSearch):
Prompts for what they want to view (menu)
Input search
Regex?
Validate menu selection
Output selection

While newSponsor (:
Asks for sponsor details. Details must be stored in a separate dict
Input following
Name
Message
Paid?
Validate
Veriffy
Output all data
Ask for y/n

The data will be passed to the functions from parameters

-------------
## Task 3

This is task 3. It's pretty short and simple, with validation. 
- [x] Separate data structures should be used to store the names of the individuals and the short messages
they would like to have written on their brass plaque. 
- [x] An output would display everything that was input for the sponsor to confirm
- [x] If errors are found, the program should allow data to be re-entered
- [x] Once complete, the data is stored and the sponsor is charged $200.


`````
def spon(spons):
    #Local init
    spon = True
    Valid = False
    global c0
    #Begin Loop
    while spon == True:
        while Valid == False:
            print("PLEASE BE AWARE THAT THIS SPONSORSHIP WILL COST $200")
            nom = input("Please enter your name:")
            msg = input("Please enter the message you would like:")
            print("PLEASE CONFIRM THE FOLLOWING DETAILS ARE CORRECT")
            print("Name:" + nom + " | Message:" + msg)
            yn = str(input("Please confirm (y/n):"))
            if yn == "y":
                spons.update({c0: [str(nom), str(msg)]}) 
                print("Sponsorship sucess!")
                spon = False
                Valid = True
                c0 = c0 + 1
            if yn == "n":
                print("Please try again")
                Valid = False
    return spons
`````

