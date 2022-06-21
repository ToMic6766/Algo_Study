d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])

# 0으로 채워진 20개의 리스트 d에 입력한 값들을 전부 넣어줌

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  # x,y 좌표 입력을 위해서 x,y를 입력받고
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0
    # x,y의 좌표에 따라 0->1 1->0 으로 바꿔주는 코드를 작성한다.
for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()
   # 출력