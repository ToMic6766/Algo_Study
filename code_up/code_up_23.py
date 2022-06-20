a, m, d, n = map(int,input().split())

total = a

for i in range(0, n-1):
    total = total * m + d

print(total) # total 값은 한번만 출력해주면된다.