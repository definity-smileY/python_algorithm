a, b = map(str, input().split())
cnt = 0

if len(a) != len(b):
    print(cnt)
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            break
        else:
            if a[i] == '8':
                cnt += 1
    print(cnt)

a = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

size = len(set(a))
dic = {a[0]:1}
print(dic)
temp = [0, len(a) - 1]
start , end = 0, 0

while (start < len(a) and end < len(a)):
    if len(dic) == size:
        if end - start < temp[1] - temp[0]:
            temp = [start, end]
        if dic[a[start]] == 1:
            del dic[a[start]]
        else:
            dic[a[start]] -= 1
        start += 1
    else:
        end += 1
        if end == len(a):
            break
        if a[end] in dic.keys():
            dic[a[end]] += 1
        else:
            dic[a[end]] = 1

print([temp[0] + 1, temp[1] + 1])