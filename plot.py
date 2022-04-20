#input pain
pain = int(input("How bad is your pain?\n1. Very bad\n2. Bad\n3. Good\n4. Very good\n5. No pain\nSelect:"))


#(s)pain
def s(pain):
    print("Pain: " + str(pain))
    if pain < 5:
        print("Good")
    elif pain < 10:
        print("Bad")
    elif pain < 15:
        print("Very bad")
    elif pain < 20:
        print("Horrible")
    else:
        print("Unbearable")

s(pain)