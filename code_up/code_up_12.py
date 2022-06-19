red,green,blue = map(int,input().split(' '))

for i in range(0,red):
    for j in range(0,green):
        for k in range(0,blue):
            print(i,j,k)
print(red*green*blue)
