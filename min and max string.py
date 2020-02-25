ma,mi='',''

l=list(input().strip('.').split(" "))
for i in l:
    if len(i)>len(ma):
        ma=i
    else:
        mi=i
for i in l:
    if len(i)<len(mi):
        mi=i
print('Largest=',ma)
print('Smallest=',mi)
