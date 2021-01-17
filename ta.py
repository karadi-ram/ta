import tabulate
import mysql.connector as db
connection=db.connect(host='localhost',user='ram',password='1234567',database='ta')
cursor=connection.cursor()

def feature():
    #enter new voter
    #remove new voter
    #create new election
     #ask what is this election for and how many candidates
    #election results
    #
while True:
    username=input('Username: ')
    password=input('Password: ')
    if username=='vote' and password == 'vote':
        feature()
    else:
        print()
        print('Username or password is wrong')
        print()
