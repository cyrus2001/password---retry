password = 'a123456'
i = 3 
while i > 0:
	pwd = input('please imput your password:')
	if pwd == password:
		print('you password is successful')
		break
	else:
		i = i - 1
		print('password wrong ! you just have' , i , 'chances')
		