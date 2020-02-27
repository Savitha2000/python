def pop(a):
    i=1
    while(i<=10):
        t=a*i
        yield t
        i=i+1
k=pop(2)
for i in range(10):
    print(next(k))
    
