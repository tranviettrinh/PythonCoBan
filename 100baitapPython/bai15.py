chuoiso=[]
x = int(input())
y = int(input())
for i in range(x,y+1):
    s =str(i)
    d = len(s)
    invalid = True
    for j in range(0,d):
        if int(s[j])%2!=0:
            invalid = False
            break

    if invalid == True :
        chuoiso.append(s)    
print(','.join(chuoiso))
