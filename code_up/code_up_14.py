d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
# 여기까지가 리스트 d를 한 리스트당 20으로 지정하고 요소는 0으로 채운 후
# 20번 찍어낸 과정

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    d[int(x)][int(y)] = 1
# 만들어진 d라는 리스트에 x와 y를 입력받아 x,y에 1이라는 숫자를 찍어낸것

for i in range(1,20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
# 여기서 1부터 시작하는 이유는 x와 y좌표가 1,1부터 시작하기때문이다
