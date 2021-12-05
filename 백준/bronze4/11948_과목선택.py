list_ = []
for i in range(6):
    a: int = input()
    list_.append(int(a))

sum_result = sum(list_[:4])
min_result = min(list_[:4])
min_result2 = max(list_[4:6])
anser = sum_result - min_result
result = anser + min_result2
print(result)