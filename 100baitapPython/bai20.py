s=0
while True:
    a = input()
    if not a:
        break
    b = a.split(' ')
    if b[0]=='D':
        s = s+int(b[1])
    elif b[0]=='W':
        s =s -int(b[1])
    else:
        pass

print(str(s))

# netAmount = 0
# # Bài tập Python 20, Code by Quantrimang.com
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print (netAmount)