cau = input()
a = len(cau)
sochu=0
soso =0
for i in cau:
    if 'A'<=i<= 'Z' or 'a'<=i<= 'z':
        sochu = sochu+1
    if '0'<=i<='9':
        soso +=1
print('so chu: '+str(sochu))
print('so so: '+str(soso))