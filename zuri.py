from datetime import datetime
import random
current_time = datetime.now()

Balance = 500000

database ={}
name=''

def receipt():
	print()
	print('-'*65)
	print('\nThank you for Banking with Zuri , you can take your Receipt.!')
	print('-'*65)
	print(f'\t \t Name : {name}')
	print()
	print(f'\t \t Your Current Balance : #{Balance}')
	print()
	print(f'\t \t \t \t  {current_time} ')
	print('-'*65)
	#transaction=input('\n Do you wish to do any transaction again? Yes or No ? : ').lower()
	#	if transaction=='yes':
			#Welcome()
	#	else:
			#exit()
	

def Main():
	global current_time, Balance,name
	print(f'Hey {name}, you have successfully logged in at {current_time}!')
	print()
	print('Select any of the option below to perform transaction: ')
	print('1. Withdrawal')
	print('2. Deposit')
	print('3. Complaint')
	Select = int(input('Enter : '))
	if Select == 1:
		Withdraw = int(input('How much do you want to Withdraw : '))
		print(f'Take your money : #{Withdraw}')
		Balance -=Withdraw
		#print(f'Your remaining balance is : #{Balance}')
		receipt()
		transaction=input('\n Do you wish to do any transaction again? Yes or No ? : ').lower()
		if transaction=='yes':
			Welcome()
		else:
			exit()
	
	elif Select ==2:
		Deposit = int(input('How much would you like to  Deposit : '))
		Balance += Deposit
		#print(f'#{Balance}')
		receipt()
		transaction=input('\n Do you wish to do any transaction again? Yes or No ? : ').lower()
		if transaction=='yes':
			Welcome()
		else:
			exit()
	
	elif Select ==3:
		Complain =input('What issue would you like to complain ? : ')
		print('Thank you for contacting Us')
		transaction=input('\n Do you wish to do any transaction again? Yes or No ? : ').lower()
		if transaction=='yes':
			Welcome()
		else:
			exit()
	
def registration():
	global name
	global database
	mini_data={}
	print('\n \t Welcome to Registration Page ')
	name = input('Enter Your Name Here : ')
	password = input('Enter Your Password Here : ')
	account_no = str(random.choice(range(1000000,9000000)))
	if account_no in database.keys():
		print('User already Exist! Try Create Another account .  ')
		registration()
	else:
		mini_data[name]=password
		database[account_no]=mini_data
		mini_data={}
		print('Registration Successful! \n')
		print('-'*65)
		print('\n Your Login Details is as follows :\n ')
		print('-'*65)
		print(f'Hi {name}, you are rewarded with #500000 for successful registration \n')
		print(f'Account Number : {account_no}')
		print(f'Password : {password}')
		print(f'\n Proceed to Login Page Please! ')
		print()
	
		Login()
		
def Login():
	global database,name
	account_nums = input('Input your Account Number : ')
	passwords = input('Input Password : ')
	
	
	if account_nums in database.keys():
		for inner in database.values():
			if passwords == inner[name]:
		#if database[account_nums].values()==passwords:
				print('Login Successful!')
				print()
				Main()
			else:
				print('Invalid Login Parameters !')
				print('Try Login Again')
				Login()
				
	else:
		print(f'User not found, Please register !')
		reg = input('Do you want to register now? Yes or No ? : ').lower()
		if reg=='no':
			print()
			Login()
		else:
			registration()
			
			
def Welcome():
	print('-'*65)
	print('\n \t\tWelcome to Zuri ATM Service')
	print('-'*65)
	print('\n Select your choice \n ')
	print('1. Login')
	print('2. Register')
	choices = int(input('Choose any of the two options : '))
	if choices == 1:
		Login()
	elif choices ==2:
		registration()
	else:
		print('\n Wrong Choices selected, Reselect your choices\n')
		Welcome()
		
Welcome()
		
		
			
		
		