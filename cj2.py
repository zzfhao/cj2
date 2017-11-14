size = 1
margin = size
position = 0
a = [0] * size
while True:
	opt,values = input().split()
	if opt == 'I':
		value = int(values)
		a[position] = value
		position = position + 1
		margin = margin - 1
		if margin == 0:
			b = [0] * size
			a = a + b
			margin = size
			size = len(a)
	
	elif opt == 'S':
		print (position,int(size))
	elif opt == 'P':
		for i in range(position):
			print (a[i])
	elif opt == 'D':
		if position != 0:
			a[position-1] = 0
			position = position - 1	
		#print (position,size)	
		if position == size/4 and position != 0:
			size = size / 2
			a = a[:-int(size)]
		elif position == 0:
			size = 1
			a = a[:-int(size)]
			
