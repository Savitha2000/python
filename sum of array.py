arr=[100,200,300,400]
p,k,sum2,sum=4,2,0,0
for j in range(k):
    sum=sum+arr[j]
sum2=sum
for i in range(k,p):
    sum2+=arr[i]-arr[i-k]
    if(sum2>sum):
        sum=sum2
print(sum)
        
    
