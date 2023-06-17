#lucky number
'''
import random

print(random.randint(1,10))

l=["tops","python","java",10,20,1,True]
print(random.choice(l))'''

import random

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)
 
for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
