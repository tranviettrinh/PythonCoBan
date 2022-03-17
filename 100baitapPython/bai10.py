# from cmath import pi


# x = int(input('gia tri x: '))
# y = int(input('gia tri y: '))
# ds=[]
# ds1 =[]
# s =0
# for i in range (0,x):
#     ds.append(ds1)
#     for j in range (0,y):
#         ds1.append()

input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# Code by Quantrimang.com
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)