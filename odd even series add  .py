//ip 20
//op
//0 0 2 1 4 2 6 3 8 4 10 5 12 6
x=int(input())
n=x//2
l=[]
a=0
b=0
m=0
l.append(a)
l.append(b)
while(m<n):
    d1=a+2
    d2=b+1
    l.append(d1)
    l.append(d2)
    a=d1
    b=d2
    m+=1
for i in l:
    print(i)
    
    
    
    
    
    
    
