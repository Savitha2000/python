a=input()
c=0
for i in a:                                        //ip {[(}])
    if i=="{":
        c+=1
    elif i=="
        c+=1
    elif i=="[":
        c+=1
    elif i=="}":
        c-=1
    elif i==")":
        c-=1
    elif i=="]":
        c-=1
if c==0:
    print("Balanced")
else:
    print("Unbalanced")
    
