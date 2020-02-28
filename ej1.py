def nb_year(p0, percent, aug, p):
    # your code
    year=0
    while p0<p:
    	p0=(percent/100)*p0+p0+aug
    	year=year+1
    return year

nb_year(1500000, 2.5, 10000, 2000000)
print("hola")