num = int(input())
sum = 0
for i in range(num+1):
    if i % 2 == 0:
        sum = sum + i
print(sum)