ds =[]
while True:
    a= input()
    if not a:
        break
    ds.append(tuple(a.split(',')))
print(ds)