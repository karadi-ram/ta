import tabulate
import mysql.connector as db
from tqdm import tqdm,trange
import time
import random
from tabulate import tabulate

connection=db.connect(host='localhost',user='ram',password='1234567',database='ta')
cursor=connection.cursor()

def logout():
	print()
	print('Logging out....')
	print()
	global condition
	condition=False
	global condition3
	condition3=False

def addvoter():
		print()
		cursor.execute('select * from voter')
		dataset=cursor.fetchall()
		lengthofset=len(dataset)
		while True:
			Name=input('Name: ')
			matched=0
			for sno,name,vid,age,father,gender,address in dataset:
				if name == Name:
					print()
					print('The name which you entered already exists')
					print()
					matched+=1
			if matched ==0:
				break
		while True:
			print()
			Age=int(input('Age: '))
			if Age < 18:
				print()
				print('Age must be 18 or above')
				print()
			else:
				break
		print()
		Father=input("Father's Name: ")
		while True:
			print()
			Gender=''		
			print('1) Male')
			print('2) Female')
			choice=int(input('Enter option(1/2): '))
			if choice == 1:
				Gender='Male'
				break
			elif choice == 2:
				Gender='Female'
				break
			else:
				print()
				print('Enter "1" for Male (or) Enter "2" for Female')
				print()
		print()
		Address=input("""Address: """)
		voterid=random.randrange(100000,1000000)
		for sno,name,vid,age,father,gender,address in dataset:
			if int(vid) == int(voterid):
				voterid=random.randrange(100000,1000000)
			else:
				pass
		sql = 'insert into voter values({},"{}","{}",{},"{}","{}","{}");'.format(lengthofset+1,Name,voterid,Age,Father,Gender,Address)
		cursor.execute(sql)
		connection.commit()
def refresh():
	cursor.execute('select * from voter')
	result=cursor.fetchall()
	newdata=[]
	counter=1
	for sno,name,vid,age,father,gender,address in result:
		mytuple=[counter,name,vid,age,father,gender,address]
		newdata.append(mytuple)
		counter+=1
	cursor.execute('truncate voter;')
	connection.commit()
	for sno,name,vid,age,father,gender,address in newdata:
		sql='insert into voter values({},"{}","{}",{},"{}","{}","{}")'.format(sno,name,vid,age,father,gender,address)
		cursor.execute(sql)
		connection.commit()
	
def feature():
	print()
	print('1) Enter new voter')
	print('2) Remove existing voter')
	print('3) update voter\'s details')
	print('4) start new election')
	print('5) Election results')
	print('6) Logout')
	option=int(input('Enter any one option: '))
	if option == 1:
		condition4=True
		while condition4:
			addvoter()
			again=input('Do you want to continue? (y/n): ')
			if again.lower() == 'y':			
				pass
			elif again.lower() == 'n':
				condition4=False
	if option == 2:
		print()
		cursor.execute('select * from voter;')
		dataset=cursor.fetchall()
		voterid=input('Enter VoterID to remove its respective details: ')
		matched=0
		for sno,name,vid,age,father,gender,address in dataset:
			if int(vid) == int(voterid):
				matched+=1
				confirm=input('Do you really want to delete the data?(y/n): ')
				if confirm.lower() == 'y':
					sql='delete from voter where vid = "{}"'.format(voterid)
					cursor.execute(sql)
					connection.commit()
					print()
					print('Data Deleted Successfully')
					refresh()
				elif confirm.lower() == 'n':
					pass
		if matched == 0:
			print()
			print('The Voter ID which you entered doesn\'t exist')
			print()

	if option == 3:
		print()
		cursor.execute('select * from voter;')
		dataset=cursor.fetchall()
		VID=input("Enter voterID to update it's detials: ")
		matched=0		
		for sno,name,vid,age,father,gender,address in dataset:
			if vid==VID:	
				matched+=1				
				print("1) Name")
				print("2) Age")
				print("3) Father's Name")
				print("4) Gender")
				print("5) Address")
				print()
				choice=int(input('Enter the option for which details should be updated: '))
				if choice == 1:
					Name=input('Enter New Name: ')
					matched=0
					for sno,name,vid,age,father,gender,address in dataset:
						if name == Name:
							print()
							print('The name already exists')
							print()	
					if matched==0:
						matched+=1
						sql = 'update voter set name = "{}" where vid = "{}";'.format(Name,VID)
						cursor.execute(sql)
						connection.commit()
						print()
						print('Name Updated ')
						print()
				if choice == 2:
					while True:
						Age=input('Enter new age: ')
						if Age < 18:
							print()
							print('Age must be 18 or more than that')
							print()
							break
						else:
							sql = 'update voter set age = "{}" where vid = "{}";'.format(Age,VID)
							cursor.execute(sql)
							connection.commit()
							print()
							print('Age updated')
							print()
				if choice == 3:
					Name=input("Enter Father's Name: ")
					sql = 'update voter set father = "{}" where vid = "{}";'.format(Name,VID)
					cursor.execute(sql)
					connection.commit()
				
				if choice == 4:
					print("1) Male")
					print("2) Female")
					Gender=input("Enter option: ")
					if Gender == "1":
						Gender='Male'
					if Gender == "2":
						Gender='Female'
					sql = "update voter set gender = '{}' where vid = '{}'; ".format(Gender,VID)
					cursor.execute(sql)
					connection.commit()
					print()
					print('Gender updated')
					print()
				if choice == 5:
					Address=input('Enter Address: ')
					sql = 'update voter set address = "{}" where vid = "{}";'.format(Address,VID)
					cursor.execute(sql)
					connection.commit()
					print()
					print('Address updated')
					print()
					
		if matched==0:
			print()
			print('The voter id which you entered doesn"t exist')
			print()
	if option == 4:
		#1ask the purpose of election
		#2enter the number of candidates
		#3ask for voter id
		#4if id is correct show the candidate list and ask to select a options
		cursor.execute('truncate election;')
		connection.commit()
		print()
		purpose=input('Enter purpose of Election: ')
		candidate=int(input('Enter number of candidates: '))		
		names=[]
		for i in range(candidate):
			alpha="Enter name of candidate number {}: ".format(i+1)
			Name=input(alpha)
			names.append(Name)
		counter=1
		for i in names:
			sql='insert into election values({},"{}","{}",{})'.format(counter,i,purpose,0)
			cursor.execute(sql)
			connection.commit()
			counter+=1 
		#tilll now candidate list of names are stored in backend
		cursor.execute('select * from election;')
		dataset=cursor.fetchall()
		setofvalues=[]		
		for sno,name,position,point in dataset:
			a=[sno,name]
			setofvalues.append(a)
		while True:
			VID=input('Enter your voterID("n" to cancel): ')
			if VID.lower()=='n':
				break
			cursor.execute('select * from voter;')
			result=cursor.fetchall()
			matched=0
			for sno,name,vid,age,father,gender,address in result:
				if vid==VID:
					for s,n in setofvalues:
						print(f"{s}) {n}")
					matched+=1
					choice=input('Enter option number of your representative("n" to stop): ')
					if choice.lower() == 'n':
						continue
					matched2=0
					for sno,name,purpose,point in dataset:
						if int(choice) == sno:
							sql='update election set point = {} where sno = {}'.format(point+1,sno)
							matched2+=1
							cursor.execute(sql)
							connection.commit()
						
					if matched2==0:	
						print()
						print('"INVALID NUMBER".Enter the respective number of your representative')
			if matched==0:
				print()
				print('INVALID VOTER ID')
				print()
	if option == 5:
			print()
			cursor.execute('select * from election;')
			result=cursor.fetchall()
			if len(result) == 0:
				print()
				print('No Election has happened')
				print()
			else:
				values=[]
				for sno,name,position,point in result:
					values.append(point)
				winner=max(values)
				values.count(winner)
				if winner == 1:	
					sql='select * from election where point = {}'.format(winner)
					cursor.execute(sql)
					winner=cursor.fetchall()
					for sno,name,position,point in winner:
						intro='In the election of "{}"'.format(position)
						anouncement='"{}" has won with {} points'.format(name,point)
						print()
						print(intro)
						print()
						print(anouncement)
						print()
				else:
					sql='select * from election where point = {}'.format(winner)
					cursor.execute(sql)
					winners=cursor.fetchall()
					head=['sno','Name','votes']
					table=tabulate(winners,headers=head,table_fmt='fancy_grid')
					print()
					print(table)
					print()
					namelist=[]
					for sno,name,position,point in winners:
						namelist.append(name)
					
					
	if option == 6:
		condition2=True
		while condition2:
			confirm=input('Do you really want to exit this application?(y/n): ')
			if confirm.lower()=='y':
				global condition
				condition=False
				condition2=False
				logout()
			elif confirm.lower()=='n':
				pass
			else:
				print('Enter "y" for yes  (or) "n" for no')
				print()
condition=True
while condition:
	username=input('Username: ')
	password=input('Password: ')
	if username == 'vote' and password == 'vote':
		print()
		print('Loading....')
		for i in trange(10):
			time.sleep(0.3)
		condition3=True
		while condition3:
			feature()
	else:
		print()
		print('Username or password is wrong')
		print()
