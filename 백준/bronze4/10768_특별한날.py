a = int(input())
b = int(input())


# if 1 <= a >= 12 and 1 <= b >= 31:
if (a, b) == (2, 18):
    print("Special")
elif (a , b) > (2, 18):
    print("After") 
else:
    print("Before")
