a, b, c = map(int, input().split())
sum_snack = a * b
if sum_snack > c:
    print(sum_snack - c)
elif sum_snack < c:
    print("0")
else:
    print("0")