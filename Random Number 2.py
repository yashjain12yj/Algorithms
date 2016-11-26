#part 2
import random
n=int(input())
k=int(input())
l = []
d = {}
for i in range(n):
	d[i]=0
while(len(l)!=k):
	temp = random.randint(0,n-1)
	if d[temp]<11:
		d[temp]+=1
		l.append(temp)
print(l)