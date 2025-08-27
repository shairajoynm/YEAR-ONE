username = 'bp_ruby'
password = 'howyoulikethat'


#1st condition
while True: 
	un1 = input("\nUsername :   ")
	p1 = input("Password :  ")

	if un1 == username and p1 == password:
		print("\n\tAccess Complete")
		break
	elif un1 == username and (not(p1 == password)):
		print("\n\tIncorrect Password. Try Again")
	elif (not(un1 == username)) and p1 == password:
		print("\n\tCan't find account name. Try Again")
	else:
		print("\n\tAccess Denied")



name = input("\nEnter your name : ")
age = int(input("Age : "))
sex = str(input("Sex : "))




#Widthraw or Deposit greetings
if sex == "Female" or sex == "female" or sex == "FEMALE" or sex == "GIRL" or sex == "GIRL" or sex == "girl" or sex == "Girl":
	print("\nGood day Ms./Mrs.", name)
elif sex == "Male" or sex == "male" or sex == "MALE" or sex == "BOY" or sex == "boy" or sex == "Boy":
    print("\nGood day Mr.", name)
#else can be used as Prefer Not to Say option
else:
	print("\nGood day", name,"!")

#Widthraw or Deposit age selector	
if age >= 18:
	print("\n\tYou can now proceed to the transaction")
else:
	print("\n\tWe're sorry, minors cannot do any transactions")
	exit()
	
#CREATE OPTIONS OF WHAT YOU WILL DO (WIDTHRAW OR DEPOSIT)
intro = input("\nAre you gonna Widthraw or Deposit?  ")

#variables for amounts
balance = 0
y = 0
x = 0
deposit = str
widthrawal = str

#amount
if intro == "Deposit" or intro == "deposit":
    x = int(input("\n\tEnter the amount that you want to Deposit :   "))
elif intro == "Widthraw" or intro == "widthraw":
	y = int(input("\n\tEnter the amount that you want to Widthraw :  "))
else:
	exit()

#confirmation
if intro == "Deposit" or intro == "deposit":
	deposit = input("\nAre you sure that you want to Deposit this amount? :  ")
elif intro == "Widthraw" or intro == "widthraw":
	widthrawal = input("\nAre you sure that you want to Widthraw this amount? : ")
else:
	exit()

x1 = 0                                       
y1 = 0

#for answers in balance
if deposit == "Yes" or deposit == "yes":
	x1 = balance + x  
	print("\nYour current balance now is", x1)
elif deposit == "No" or deposit == "no":
	exit()
elif balance < y :
	print("\n\tYour balance is not enough to do this transaction")
elif widthrawal == "Yes" or widthrawal == "yes":
	y1 = balance - y
	print("\nYour current balance now is", y1)
elif widthrawal == "No" or widthrawal == "no":
	exit()
else:
	exit()

#for the last
if deposit == "Yes" or deposit == "yes" and sex == "Female" or sex == "female" or sex == "FEMALE" or sex == "GIRL" or sex == "GIRL" or sex == "girl" or sex == "Girl": 
	print("\n\tThank you Ms./Mrs.", name, "for transacting with us!")
	exit()
elif deposit == "Yes" or deposit == "yes" and sex == "Male" or sex == "male" or sex == "MALE" or sex == "BOY" or sex == "boy" or sex == "Boy": 
	print("\n\tThank you Mr.", name, "for transacting with us!")
elif balance < y and sex == "Female" or sex == "female" or sex == "FEMALE" or sex == "GIRL" or sex == "GIRL" or sex == "girl" or sex == "Girl":
	print("We're sorry Ms./Mrs.", name,"we hope to see you transacting with us again")
elif balance < y and  sex == "Male" or sex == "male" or sex == "MALE" or sex == "BOY" or sex == "boy" or sex == "Boy":
    print("We're sorry Ms./Mrs.", name,"we hope to see you transacting with us again")
else:
	exit()



