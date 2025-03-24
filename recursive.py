def factorial(n):
	if n==0:
		return(1)
	return(n*factorial(n-1))
	
print(factorial(5))


def exponentiation(a,b):
	if b==0:
		return(1)
	return(a*exponentiation(a,b-1))

print(exponentiation(100,2))


def expomod(b,a,m):
	if a==0:
		return 1
	return(b*(expomod (b,a-1,m) % m )% m)

print(expomod(3,2,9))



def mexp(b,a,m):
	if a==0:
		return 1
	q=a//2
	if a%2:
		return((mexp(b,q,m) % m) * (mexp(b,q,m) % m ) * ((b % m) % m) % m )
	else:
		return( (mexp(b,q,m) % m) * (mexp(b,q,m) % m )  % m  ) 



print(mexp(5,2,7))



def search(i,j,x,A):
	if i>j:
		return(False)
	if A[i]==x:
		return(i)
	return(search(i+1,j,x,A))

A=[0,1,2,3,4,5,6,8]
print(search(0,7,2,A))

def merge(A,p,q,r):
	nl=(q-p)+1
	nr=(r-q)
	Al=list(range(nl))
	Ar=list(i for i in range(nr))

	for i in range(nl):
		Al[i]=A[i+p]
	for i in range(nr):
		Ar[i]=A[q+1+i]

	i=0
	j=0
	k=p

	while (i<nl and j<nr):
		if Al[i]<Ar[j]:
			A[k]=Al[i]
			i+=1
		else:
			A[k]=Ar[j]
			j+=1
		k+=1

	while i<nl:
		A[k]=Al[i]
		i+=1
		k+=1

	while j<nr:
		A[k]=Ar[j]
		j+=1
		k+=1

def merge_sort(A,p,r):
	if p>=r:
		return
	q=(p+r)//2
	merge_sort(A,p,q)
	merge_sort(A,q+1,r)
	merge(A,p,q,r)

A=[3,321,2,0,0,1,2,4,5]

merge_sort(A,0,8)
print(A)



def binary_search(A,x,p,r):
	if p>r:
		return (0)
	q=(p+r)//2
	if A[q]==x:
		return (q)
	elif (A[q]<x):
		return(binary_search(A,x,q+1,r))
	else:
		return(binary_search(A,x,p,q-1))


print( binary_search(A,1,0,8) )



def fib(n):
	if n==0:
		return (0)
	if n==1:
		return (1)
	return(fib(n-1)+fib(n-2))
print(fib(3))


def iteratve_fib(n):
	if n==0:
		return 0
	else:
		x=0
		y=1
	for i in range( n-1):
		z=x+y
		x=y
		y=z
	return y

print(iteratve_fib(10))