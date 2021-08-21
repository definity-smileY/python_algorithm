a = int(input())


# if a % 10 == 0:
#     a_list = [0] * 3

#     a_list[0] = a // 300
#     a %= 300

#     a_list[1] = a // 60
#     a %= 60
    
#     a_list[2] = a // 10
#     a %= 10

#     print(*a_list)
# else:
#     print(-1)



if a % 10 != 0:
    print(-1)

else:
    print(a // 300, end=" ")
    print((a % 300) // 60, end=" ")
    print(((a % 300) % 60) // 10)

