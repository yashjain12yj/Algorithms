#part 1

import random

n=int(input())
k=int(input())
l = []
for i in range(n):
	l.append(i)
max = n-1
while(max>0):
	temp = random.randint(0,max)
	l[temp],l[max] = l[max],l[temp]
	max -= 1
l1=[]
for i in range(k):
	l1.append(l[i])
print(l1)