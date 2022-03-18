a = int(input())
s=0
x=[]
for i in range(1,9):
    x.append(i*str(a))
for j in x:
    s = s+int(j)
print(s)