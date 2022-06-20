# 등차수열
a,d,n = map(int,input().split())

sum = a

for i in range(0, n-1): # n-1 까지 하는 이유는 0부터시작하기때문
    sum = sum + d # sum값에 계속해서 d값을 더해줌 등차수열

print(sum) # 결국 마지막인 n값에 도달하면 그 값을 출력한다. # n값은 몇번째수인지를 나타내고있기때문에.