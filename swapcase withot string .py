class cse:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def swap(self):
        self.a,self.b=self.b,self.a
a,b=32,56
p=cse(a,b)
cse.swap(p)
print(p.a,p.b)

--------------------------------------------------
class cse: 
       def swap(self,a,b):
        self.a=a
        self.b=b
        self.a,self.b=self.b,self.a
a,b=32,56
p=cse()
cse.swap(p,a,b)
print(p.a,p.b)






