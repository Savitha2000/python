sum=0
a=int(input())
temp=a
while(a):
    i=1
    f=1
    r=a%10
    while(i<=r):
        f=f*i
        i=i+1
        sum=sum+f
        a=a//10
if (sum==temp):
    print("The number is a strong number")
    
else:
    print("The number is not a strong number")
    
    
            
        
        
            
