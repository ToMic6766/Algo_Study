num = int(input())
sum = 0
count = 0
while(True):
    sum = count + sum
    count += 1
    if sum >= num:
        print(sum)
        break