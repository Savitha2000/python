a=int(input())
if a<10 or a>99:
    print("Invalid Input")
else:
    first=a//10
    last=a%10
    sum=first+last
    spl=first*last
    if sum+spl==a:
        print(a,"is a special number")
    else:
        print(a,"not a special number")
        
        
    
