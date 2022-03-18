cau = input()
chuThuong=0
chuHoa =0
for i in cau:
    if i.isupper() :
        chuHoa = chuHoa+1
    elif i.islower():
        chuThuong =chuThuong+1
    else:
        pass
print('Hoa: '+str(chuHoa))
print('Thuong: '+str(chuThuong))