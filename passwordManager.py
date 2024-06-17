import random

def WriteFile(encrypterPassword, account):
    with open('text.txt', 'w') as wf:
        wf.write(f"\n\n{account} : {encrypterPassword} \n")

def appendFile(encrypterPassword, account):
    with open('text.txt', 'a') as af:
        af.write(f"\n\n{account} : {encrypterPassword} \n")

def checkFileCont():
    with open('text.txt', 'r') as cf:
        if cf.read() is None:
            return False
        else:
            return True

def readFile():
    with open('text.txt', 'r') as rf:
        text_content = rf.read()
        
        print(text_content)

def getAccountPass(account):
    with open('text.txt', 'r') as rf:
        for line in rf:
            if line.startswith(account):
                return line.strip()

def generateRandomPassword():
    randomGenPassword = ""

    for i in range(11):
        randomAsciiValue = random.randint(33, 126)
        randomGenPassword += chr(randomAsciiValue)
        
    return randomGenPassword


def cipherShifter(loginPassword):
    tempVar = 0
    while (loginPassword > 9):
        tempVar = loginPassword % 10
        loginPassword //= 10
        loginPassword += tempVar
    return loginPassword

def encrypterPassword(password, cipherShifter):
    encrypterNewPassword = ""
    
    for char in password:
            encrypterNewPassword += chr((ord(char) + cipherShifter))
           
    return encrypterNewPassword

def dencrypterPassword(password, cipherShifter):
    dencrypterNewPassword = ""
    
    for char in password:
            dencrypterNewPassword += chr((ord(char) - cipherShifter))
           
    return dencrypterNewPassword

if __name__  == "__main__":
    print("\n\n----- Welcome to password manager -----\n\n")
    loginPassword = int(input("Enter your pin : "))
    cipherShifter = cipherShifter(loginPassword)
    print("""
          
          
        ---OPTIONS---

1) To generate password for you account , enter (1)
2) To find a saved password under the account , enter (2)
3) To manually enter you password for you accounts (3)
          
          
          """)
    
    options = str(input("Enter an option : "))
    
    if options == "1":
        account = str(input("\n\nYour are creating a password for : "))

        randomPassword = generateRandomPassword()
        print(f"\n\nThis is your unencrypted generated password for {account} account: {randomPassword}")
        
        encrypterPassword = encrypterPassword(randomPassword, cipherShifter)
        
        print(f"\n\nThis is your encrypted password for {account} account: {encrypterPassword}")
        
        appendFile(encrypterPassword, account)
        
        print("\n\nThe encrypted password is now saved , in order to use your password , you will need your password to decrypt it")
        
    elif options == "2":
        readFile()
        isDecrypt = str(input("Do you want to decrypt an account password (yes/no):"))
        if isDecrypt.lower() == "yes":
            account = str(input("\n\nName an account you want to decrypt it password: "))
            list = getAccountPass(account).split(":")
            accountPass = dencrypterPassword(list[1], cipherShifter)
            print(f"\n\nThis is you encrypted password for {account} : {accountPass}")
        else:
            print("\n\nYou have exited the program, bye!")
    elif options == "3":
        account = str(input("\n\nYour are saving a password for the account : "))
        passwordManual = str(input(f"\n\nEnter you password for the {account} account : "))
        print(f"\n\nThis is your unencrypted generated password for {account} account: {passwordManual}")
        
        encrypterPassword = encrypterPassword(passwordManual, cipherShifter)
        
        print(f"\n\nThis is your encrypted password for {account} account: {encrypterPassword}")
        
        appendFile(encrypterPassword, account)
        
        print("\n\nThe encrypted password is now saved , in order to use your password , you will need your password to decrypt it")
        
        
        
            
            
            
            
            
            
            

        
        
        
        
        
        
        

        
        
        