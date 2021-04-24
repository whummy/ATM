#register
    #first name,last mane, email,password
    #generate user account

#login
#-accountnumber and password

# bank operations
#initializing the system


import random


database = {
    7034320246: ['ola','wunmi','ola@gmail.com', 'olusola', 1000, 7034320246]
}  #dictionary

def init():
    
    print("Welcome to Solz bank")

    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no)\n"))

    if(haveAccount==1):
        
        login()
    elif(haveAccount == 2): 
        
        register()
    else:
        print("You have selected an invalid option")
        init()
            

def login():
    print("********Login********")

    accountNumberFromUser = int(input("What is your account number?\n"))
    password = input("Enter password\n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                return

    print('Invalid account or password')

    login()

    

def register():

    print("******Register******")

    email = input("Enter your email address?\n")
    first_name = input("Enter your first name?\n")
    last_name = input("Enter your last name?\n")
    password = input("create a password\n")

    accountNumber = generateAccountNumber()

    database[accountNumber] =[first_name, last_name, email, password, 0, accountNumber]

    print("Your Account Has been Created")
    print("== ==== ====== ===== ===")
    print ("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    login()
    
def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selectedOption = int(input("what would you like to do? (1) deposit (2) withdrawal (3) complaint (4) Logout (5) exit \n"))

    if(selectedOption == 1):
        depositOperation(user)
    elif(selectedOption == 2):
        withdrawalOperation(user)
    elif(selectedOption == 3):
        complaint()
    elif(selectedOption == 4):
        logout(user)
    elif(selectedOption == 5):
        exit()
    else: 
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation(user):
    cash_withdrawal = int(input('How much would you like to withdraw?\n'))
    if (cash_withdrawal <= getCurrentBalance(user)):
        new_bal = getCurrentBalance(user) - cash_withdrawal
        user[4] = new_bal
        database[user[5]] = user
        print("Take your cash")
        print("your new balance is", new_bal)
    else:
        print('Insufficient Balance')

    bankOperation(user)

def depositOperation(user):  
    cash_deposit = int(input('How much would you like to deposit?\n'))
    new_bal = cash_deposit + getCurrentBalance(user)
    user[4] = new_bal
    database[user[5]] = user
    print("your new balance is", new_bal)
    bankOperation(user)


def complaint():
    input('What issue will you like to report?\n')
    print("Thank you for contacting us")


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def getCurrentBalance(userDetails):
    return userDetails[4]


def logout(user):
    selectedOption = int(input("Are you sure you want to log out? (1) yes (2) no\n"))
    if(selectedOption == 1):
        exit()
    else:
        bankOperation(user)

    


#### ACTUAL BANKING SYSTEM  ####
#print(generateAccountNumber())
init()