def hanoi(n):
	if n==1:
		return(1)
	return(2*(hanoi(n-1))+1)

# print(hanoi(64))


def consecutive_0(n):
	if n==2:
		return(3)
	if n==1:
		return(2)
	return (consecutive_0(n-1)+consecutive_0(n-2))

print(consecutive_0(5))