n=int(input())
d=1
nu=0
for i in range(1,n+1):
    d=d*i
for i in range(1,n+1):
    nu+=d//i
i=1
while(i<=n):
    if(nu%i==0 and d%i==0):
        d=d//i
        i=1
    i=i+1
print(f'sum of a series:{nu}/{d}=>{nu/d:.2f}')
    /////ip:3
    
///op:sum of a series:11/6=>1.83
