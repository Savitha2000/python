l=[2,4,3,1,7,5]
n=len(l)
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]>l[i]:
            k=l[i]
            l[i]=l[j]
            l[j]=k
for i in range(0,n):
    print(l[i],end=" ")
    
