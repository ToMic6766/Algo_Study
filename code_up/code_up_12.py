num = int(input())
count = 0
sum = 0
while True:
    count += 1
    sum += count
    if sum >= num:
        print(count)
        break