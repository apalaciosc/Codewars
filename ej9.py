#Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
#Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

def reverse_number(n):
    n=str(n)
    var=[]
    c=0
    res=''
    for x in n:
    	c-=1
    	var.insert(c,x)
    if var[-1]=='-':
    	var.pop(-1)
    	var.insert(0,'-')
    for x in var:
    	res=res+x
    return int(res)


print(reverse_number(-12345))