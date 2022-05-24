number_of_verify = list(map(int,input().split()))
for i in range(len(number_of_verify)):
    number_of_verify[i] = number_of_verify[i] * number_of_verify[i]
sum_list = sum(number_of_verify)
verifycation = sum_list % 10
print(verifycation)

# 정석 답안
# res = 0
# for n in list(map(int, input().split())):
#     res += n**2
# print(res%10)