x=int(input())
n=x//2
l=[]
a=1
b=1
m=1
l.append(a)
l.append(b)
while(m<n):
    d1=a*2
    d2=b*3
    l.append(d1)
    l.append(d2)
    a=d1
    b=d2
    m+=1
for i in l:
    print(i)
    
