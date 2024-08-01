#a = int(input('請輸入三角形邊長:'))
a=4
#for i in range(0,a):
#    print(' '*(a-i-1),'*'*(i*2+1))

for i in range(0,a):                
    for j in range(a-i,1,-1):       
        print(' ',end='')
    for k in range(0,i * 2 + 1,1):  
        print('*',end='')
    print()