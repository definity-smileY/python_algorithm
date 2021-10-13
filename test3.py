# from decimal import Decimal


# # # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # # result = [i <= 5 for i in range(a)]
# # # print(result)



# # # result = [i <= 0 for i in [1, True, False, True, False, True, False, 1] if i is not None]
# # # print(result)

# # # a = [i >= 0 for i in any([1, 0, None, 1, 0, None]) if i is not None]
# # # print(a)

# # # 목적은 에러를 내기위함 -> 왜냐? 지정한 값을 제외한 값들이 들어오면 안되기 떄문에
# # test_result = any([ i <= 0 for i in [1, 1, None, 1, 1, None] if i is not None ])

# # # print(any(test_result))
# # if test_result:
# #     raise ValueError("daskdmasldkmadl;kmasdl;asm")


# # """
# # [Test_Case] input값으로 가격이 제대로 들어오는지에 대한 세부 로직 짜보기
# # """

# # # 가격은 양수여야하며, 0은 안되고, Default값으로 None을 지정했다.

# # test_case = any( i <= 0 for i in [2, None, 1, 2, None, 1,] if i is not None )

# # # True일 경우 조건문을 타서 에러를 발생
# # if test_case:
# #     ValueError("discount or minimum data should be positive")

# # result = 9600
# # print(result >= 10000 * Decimal("0.95"))

# [
#     (
#         [
#             "Coupon",
#             {'[user_key]' : '[user_value]'},
#         ]

#     ),
#     (
#         [
#             "Coupon",
#             {'[user_key]' : '[user_value]'},
#         ]

#     )
#     (
#         [
#             "Coupon",
#             {'[user_key]' : '[use   r_value]'},
#         ]

#     )
#     (
#         [
#             "Coupon",
#             {'[user_key]' : '[user_value]'},
#         ]

#     )
    
# ]

a = [1, 2, 3, 4, 5, 6,]
print(a[-1])