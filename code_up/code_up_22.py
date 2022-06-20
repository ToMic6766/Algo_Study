# 등비수열
a, r, n = map(int,input().split())
mul = a # 초기값지정

for i in range(0, n - 1):
    mul = mul * r # mul에 계속하여 r을 곱하는 방식
print(mul)