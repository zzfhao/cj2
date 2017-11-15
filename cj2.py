size = 1
margin = size
position = 0
a = [0] * size
opt = ''
value = 0		
while True:
	try:
		# this part enable the variable number of input in the same line
		# the split function split the input by space into several strings and store them in the same list
		input_opts = input().split()
		# get the number of strings from the input
		num_elmts = len(input_opts)
		# if there are two input, which is the case for insert operation, take the first as operator and second one as value
		if(num_elmts == 2):
			# get the first string from the list
			opt = input_opts[0] 
			# get the second string from the list
			value = input_opts[1]
		# when there is not two input, which means <delete>, <print> and <show> operations
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
			# print all elements in the same line!!
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