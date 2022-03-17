ds =[]
a = int(input('so nguyen n can nhap: '))
for i in range(1, a+1):
    s = i*i
    ds.append(str(i)+':'+str(s))
print('{'+','.join(ds)+'}')

d =dict()
for u in range(1, a+1):
    d[u]=u*u
print(d)