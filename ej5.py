def reverser(sentence):
	var = ''
	res=[]
	resfinal=''
	arr=sentence.split(' ')
	if sentence==' ':
		return ' '
	if len(arr)>1:
		for h in arr:
			for x in h:
				var=x+var
			res.append(var)
			var=''
		for x in res:
			resfinal=resfinal+x+' '
		resfinal=resfinal.strip()
		if arr[-1]=='':
			resfinal=resfinal+' '
		if arr[0]=='':
			resfinal=' '+resfinal
	else:
		for c in sentence:
			resfinal=c+resfinal
			resfinal=resfinal.lstrip()
	return resfinal

print(reverser(' '))