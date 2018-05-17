#Jumping number is the number that All adjacent digits in it differ by 1.
#Task
#Given a number, Find if it is Jumping or not .

def jumping_number(number):
	number=str(number)
	c=0
	diff=0
	if len(number)==1:
		return "Jumping!!"
	else:
		while c<len(number):
			if c<=len(number)-2:
				diff=int(number[c])-int(number[c+1])
				if diff==1 or diff==-1:
					c+=1
				else:
					return "Not!!"
			else:
				return "Jumping!!"

print(jumping_number(1))    	