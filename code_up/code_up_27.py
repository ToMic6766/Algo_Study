m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)
# 12 x 12 사각형의 리스트를 0으로 채워서 작성한다.
for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i+1][j+1]=int(a[j])
#1,1 좌표부터 11,11가지의 좌표까지 입력
x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break
# 바깥쪽은 1로 채워져있으니 2,2좌표부터 탐색시작 지나간곳은 9로 변경
  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
    break
# 장애물을 만났거나 또는 x,y가 9라면 종료하라 (즉 오른쪽 끝에 도착했다면 종료한다의 의미와 또는 이미 지나간길이니 가지못한다는 의미)
  if m[x][y+1] != 1 :
    y += 1
  elif m[x+1][y] != 1 :
    x += 1
# 탐색 후 만약 1이 아니면 다음으로 진행
# 오른쪽과 아래쪽으로 계속하여 이동한다.

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
# 출력