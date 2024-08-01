n=int(input('請輸入一個正整數：'))
count=0
for i in range(2, n + 1):
    prime = True
    for j in range(2, i ):
        if i % j == 0: # 可以整除的話 => 較小的數可以做為較大的數的因數
            prime = False
            break
    if prime :
        print(i)
        count+=1
print(f"總共有{count}個質數")
