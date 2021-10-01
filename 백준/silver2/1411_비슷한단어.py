# 5
n = int(input())
# ['aa', 'ab', 'bb', 'cc', 'cd']
list = [input() for _ in range(n)]
cnt = 0

for i in range(0, n-1):
    for j in range(i+1, n):
        s1=list[i] 
        s2=list[j]
        flag = True
        if len(s1) == len(s2):
            # A-Z = 26
            visit1 = [0]*26
            visit2 = [0]*26
            for k in range(len(s1)):
                # 유니코드                
                idx1=ord(s1[k])-ord('a')
                idx2=ord(s2[k])-ord('a')
                if visit1[idx1]==0 and visit2[idx2]==0:
                    visit1[idx1]=s2[k]
                    visit2[idx2]=s1[k]
                elif visit1[idx1]!=s2[k]:
                    flag=False
                    break
        if flag:
            cnt+=1        
print(cnt)

"""
두 쌍의 길이만 맞으면 비교로직타기
"""
