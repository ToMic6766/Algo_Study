num = int(input())
call_num = list(map(int,input().split()))

for i in range(num-1, -1, -1):
    print(call_num[i], end=' ')