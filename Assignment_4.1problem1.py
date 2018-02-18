
# coding: utf-8

# In[ ]:


class Assign():
    def _init_(self,s,a,b,c):
        self.s=s
        self.a=a
        self.b=b
        self.c=c

class Calculate(Assign):
    def _init_(self, *args):
        super(Calculate,self)._init_(*args)
        
    def area(self):
        self.area=(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5
        return self.area
    
calculate=Calculate(1,2,3,4)
print(calculate.area())

