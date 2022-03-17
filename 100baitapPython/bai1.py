from ntpath import join


ds = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        ds.append(str(i))
for y in range(0,len(ds)-1):
    print(ds[y] +',')
s = ','
print(s.join(ds))
