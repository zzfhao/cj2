size = 1
margin = size
position = 0
a = [0] * size
opt = ''
value = 0		
while True:
	try:
		input_opts = input().split()
		num_elmts = len(input_opts)

		if(num_elmts == 2):
			opt = input_opts[0] 
			value = input_opts[1]
		else:
			opt = input_opts[0]
			 

		if opt == 'I':
			#print (position)			
			if margin == 0:
				b = [0] * size
				a = a + b
				margin = size
				size = int(len(a))
			a[position] = value
			position = position + 1
			margin = margin - 1

		
		elif opt == 'S':
			print (position,size)
		elif opt == 'P':
			#for i in range(position):
				#print (a[i])
			print(*a[:position])
		elif opt == 'D':
			if position != 0:
				a[position-1] = 0
				position = position - 1	
			#print (position,size)	
			if position == size/4 and position != 0:
				size = int(size / 2)
				a = a[:-size]
			elif position == 0:
				size = 1
				a = a[:-size]
	# use exception for EOFError to avoid empty input when terminate programme
	except EOFError:
		break