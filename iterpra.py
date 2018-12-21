#!/usr/bin/python
#coding:utf-8
class i_pra():
    def __iter__(self):
        #print "iter"
        return self
    def __init__(self,n):
        #print "init"
        self.flag=n
        self.temp=self.flag
        self.a,self.b=0,1
    def next(self):
        #print "next"


        if self.temp>=0:
            '''
            iii=self.a
            self.temp-=1
            temp=self.a+self.b
            self.a=self.b
            self.b=temp
            return iii
            '''
            self.temp-=1
            temp,self.a,self.b=self.a,self.b,self.a+self.b
            return temp

        else:
            #下次使用该对象的时候，仍然可用，否则的话一个对象只能完整遍历一次
            self.a=0
            self.b=1
            self.temp=self.flag
            raise StopIteration()
a=i_pra(10)
data=[t*2 for t in a]
print data


print [t*199 for t in a]
'''
a.temp=10
a.a=0
a.b=1
'''
for i in a:
    print i
            
        
