a = input().split(',')
b=[]
for i in a:
    if int(i)%2==1:
        b.append(i)
print(','.join(b))