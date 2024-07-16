# # 구구단 3단 출력, 3 x 3 = 9 형태로 출력
# for num in range(1, 10):
#     a = 3*num
#     print("3 x", num, "=", a)

# # for 반복문 2번 사용해서 2차원 리스트의 요소를 모두 출력해라
# num_list = [[10,50], [20,40], [30,60], [40,70]]
# for num in num_list:
#     for ber in num:
#         print(ber)

# # 이중 리스트의 평균값
# my_list = [[100,200], [400,800], [1000,1400]]
#
# for number in my_list:
#     var = 0
#     for list in number:
#         var = var + list
#     print(var/len(number))

i = 0
while i < 10:
    i = i + 1
    print("나무를",i, "번 찍었습니다.")
print("나무가 넘어갑니다!")


