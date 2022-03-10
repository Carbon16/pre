h=0
s=0
g=0


hat = int(input())
scarf = int(input())
gloves = int(input())


if int(hat) >= 1:
    h = 1
if int(scarf) >= 1:
    s = 1
if int(gloves) >= 2:
    g = 1

if h + g + s >= 2:
    print("toasty")
if h + g + s < 2:
    print("cold")

lft1 = hat-1
lft2 = scarf-1
lft3 = gloves-2
if lft1 <= 0:
    lf1 = 0
if lft2 <= 0:
    lf2 = 0
if lft3 <= 0:
    lf3 = 0

print(lft1 + lft2 + lft3)