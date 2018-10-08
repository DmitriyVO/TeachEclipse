import os
import qu
from qu import qsort



#3434
#5656
a='Box'
b='2'
a+=b;
print(a)
array=[10,4,6,7,8,3,5]
print(array)
print('MODUL')
array=qu.qsort(array)
print(array)

k1=['105','103']

print("Hello "+os.getcwd()+'\n')


mass='#&105;#&105;#&105;#&105;#&105;'
print(mass)
mass=mass.replace('#', '',).replace('&', '').replace(';',' ').strip().split(' ')
q1 = [int(i) for i in mass]
q2=[chr(c) for c in q1]
print(q2)


nums = [4, 1, 6, 3, 2, 7, 8]
print(nums)
n = 1
while n < len(nums):
    for i in range(len(nums) - n):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i+1] = nums[i + 1], nums[i]
#             print(nums[i])
#             print(nums[i+1])
#             print(nums)
    n +=1
print(nums)






obmen = [1,7,3]
print(obmen)

obmen[0], obmen[1], obmen[2]  = obmen[1], obmen[2],obmen[0]

a='QWE'
a1='ASD'
print(a1,a)
a,a1 = a1,a
print(a1,a)


print(obmen)

K=[5,8,22,3,4,5,7,34,6,8]
print(K)
def qsort1 (Z):
    if Z :return qsort1([x for x in Z if x<Z[0]])+[x for x in Z if x==Z[0]]+qsort1([x for x in Z if x>Z[0]])
    return[]
print(qsort1(K))

class Desc:
              
    @staticmethod
    def pop(value):
        return value * 1000
     
        def get__ (self, obj, tupe):
            return self.value
     
        def set__ (self, obj, value):
            self.value = int(value)*4


class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)*10    
        
        
class Iam:
    xyi= Desc()
    piz=Celsius()



dima = Iam()
dima.piz=12
dima.xyi=1000
print(dima.piz,"piz")
print(dima.xyi)  
dima.xyi=100
print(dima.xyi)

