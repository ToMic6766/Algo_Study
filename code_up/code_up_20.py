num = int(input())

for i in range(0,num+1):
    if i % 3 == 0:
        continue
    else:
        print(i,end=' ')