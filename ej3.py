def square_digits(num):
    c=0
    cad=''
    while c<len(str(num)):
    	add=''
    	add=str(num)[c]
    	add=int(add)
    	cad=cad+str(add**2)
    	c+=1
    return int(cad)

print(square_digits(9119))