
def greatest_i(start,finish,n):
	p=[]
	for i in range(n,-1,-1):
		for j in range(i-1,-1,-1):
			if start[i]>=start[j] and finish[j]<=start[i]:
				p.append(j+1)
				break
			if j==0:
				p.append(0)
				break
	p.append(0)
	p=p[::-1]
	return p
def schedule(start,finish,attendance,p,n):
	if n==-1:
		return 0
	return(max(attendance[n]+schedule(start,finish,attendance,p,p[n]-1),schedule(start,finish,attendance,p,n-1)))

start=[9,8,7,10,13]
finish=[10,10,13,15,17]
attendance=[10,4,7,8,14]
p=greatest_i(start,finish,4)
print(p)

print(schedule(start,finish,attendance,p,3))





