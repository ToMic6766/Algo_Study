# w, h, b = map(int,input().split(' '))

# print(round(w*h*b/8/1024/1024,3), "MB")

w,h,b = input().split()
res=int(w)*int(h)*int(b)/1024/1024/8

print('%.2f'%res,"MB")