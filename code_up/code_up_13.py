n = int(input())
call_num = list(map(int,input().split()))

min = call_num[0]
for i in range(0,n):
    if call_num[i] < min:
        min = call_num[i]

print(min)