input_H =input()
input_H = int(input_H,16)
for i in range(1,16):
    print('%X'%input_H, '*%X'%i, '=%X'%(input_H*i), sep='')