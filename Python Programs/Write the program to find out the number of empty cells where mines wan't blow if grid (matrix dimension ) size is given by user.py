a,b=input().split('x')
a,b=int(a),int(b)
count=0
for i in range(0,a):
    for j in range(0,b):
        if (i+j)%2!=0:
            count+=1
print(count)
