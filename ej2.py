def solution(s):
	arreglo=[]
	c=0
	if len(s)%2==0:
		while c<len(s):
			add=s[c:2+c]
			arreglo.append(add)		
			c+=2
	else:
		while c<len(s):
			add=s[c:2+c]
			arreglo.append(add)
			c+=2
		arreglo[-1]=arreglo[-1]+"_"
	return arreglo
    

print(solution('asdfadsfx'))