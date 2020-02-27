a,b=map(int,input().split(" "))
l=0
p=0
for i in range(a,b+1):
    l=0
    temp=i                      
    ld=0
    lg=len(str(i))
    while(i>0):
        ld=i%10
        i=i//10
        l+=ld**lg
    if l==temp:
        print(l,end=" ")
        p+=1
if p==0:
    print("NO")
