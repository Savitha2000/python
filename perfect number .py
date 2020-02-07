n=int(input())
sum=0
for i in range(1,n+1):
    if i%n==0:
        sum=sum+i
        if sum==n:
           print("The the number is perfect")
        else:
           print("The number is not perfect")
        
