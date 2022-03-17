a = int(input('giai thua cua: '))
s = 1
for i in range(1,a+1):
    s = s*i
if s==0:
    s=1
    print(s)
else:
    print(s)

def giaithua(x):
    if x ==0:
        return 1
    else:
        return x*giaithua(x-1)
print(giaithua(a))
        
