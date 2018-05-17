def breakChocolate(n, m):
	if (n==1 and m==1) or n==0 or n==0:
		return 0
	else:
		res=(n*m)-1
		return res

  
print(breakChocolate(5, 5))