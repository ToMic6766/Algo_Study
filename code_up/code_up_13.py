# h,b,c,s = map(int,input().split(' '))
# result = str((h * b * c * s)/8)
# mystring = result[0:2]
# print(mystring + "MB")



h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)

print(round(h*b*c*s/8/1024/1024, 1), "MB")