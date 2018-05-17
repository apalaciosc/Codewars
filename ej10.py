#Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate the men from the boys
#Notes
#   Return an array/list where Even numbers come first then odds
#   Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
#   Array/list size is at least 4 .
#   Array/list numbers could be a mixture of positives , negatives .
#   Have no fear , It is guaranteed that no Zeroes will exists . !alt
#   Repetition of numbers in the array/list could occur , So (duplications are not included when separating).

def men_from_boys(arr):
	#your code here
	par=[]
	impar=[]
	final=[]
	for x in arr:
		if x%2==0:
			par.append(x)
		else:
			impar.append(x)
	par=list(set(par))  #Eliminar repetidos
	impar=list(set(impar))  #Eliminar repetidos
	par.sort()  #ordenar ascendente
	impar.sort(reverse=True) #ordenar descendente
	final=par+impar
	return final

#Example
print(men_from_boys([2,2,43,95,90,37]))