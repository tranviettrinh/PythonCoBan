value =[]
iteams =input("Nhap cac so nhi phan: ").split(',')
for p in iteams:
    intp = int(p,2)
    if  intp%5==0:
        value.append(p)
print(','.join(value))
