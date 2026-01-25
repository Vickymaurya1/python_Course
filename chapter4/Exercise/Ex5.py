a = [7,0,8,0,0,9, 0]
result = 0

for i in range(len(a)):
    if(a[i] == 0):
        result +=1
    else:
        continue
print(result)