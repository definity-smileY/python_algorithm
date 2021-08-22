a = int(input())
for _ in range(a):
    doller = float(input())
    b = doller - (doller * 0.2)
    
    print("${:.2f}".format(b))
    