H, M, S = map(int, input().split())
R = int(input())

Result_S = (S+R) % 60
Return_S = (S+R) // 60

Result_M = (M+Return_S) % 60
Return_M = (M+Return_S) // 60

Result_H = (H+Return_M) % 24

print(Result_H, Result_M, Result_S)