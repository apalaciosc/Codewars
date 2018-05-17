#A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5 
#Task
#Given a number determine if it special number or not . 

def special_number(number):
    validos=[]
    #Llenando validos
    for x in range(0,6):
    	validos.append(x)
    
    number=str(number)
    for x in number:
    	if int(x) not in validos:
    		return "NOT!!"
    return "Special!!"

print(special_number(709))