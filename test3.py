# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = [i <= 5 for i in range(a)]
# print(result)



result = [i <= 0 for i in [1, True, False, True, False, True, False, 1] if i is not None]
print(result)

