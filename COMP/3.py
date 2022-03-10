pin = str(input())
for i in range(0,3):
    if pin[i] >= pin[i +1]:
        print(pin[i +1])
