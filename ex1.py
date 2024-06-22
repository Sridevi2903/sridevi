def passportVerification():
    print("\n\nPassport Verification Process")
    pp=input("\nEnter Your Passport Number: ")
    visa=input("\nEnter Your Visa Number: ")
    print("\nYou are Eligible to Immmigration, please Wait")

def covid():
    print("\nCovid Checking Process")
    covid = input("\nYour Covid result is Positive or Negative: ")
    if covid == "negative":
        print("\nYou are eligible to Next process of checking, please wait")
    elif covid == "positive":
        print("\nYou are Not eligible to travel, Because Your a Covid Attacked Person")
    else:
        print("\nInvalid Details, Try Again")

def Immigration():
    print("\n\nImmigration Checking Process")
    eligible=input("\nEnter Your Eligible paper Number: ")
    passport=input("\nEnter Your Passport Number: ")
    visa=input("\nEnter Your Visa Number: ")
    aadhar=input("\nEnter Your Aadhar card Number: ")
    print("\nYou are Eligible to travel,Please Wait to Luggage Checking")

def Luggage():
    print("\n\nLuggage Checking Process")
    print("\nPlease put on the luggage into the Weight machine")
    weight=input("\nEnter The Luggage Weight: ")
    if weight<="20":
        print("\nYou can keep your luggage with you")
    elif weight>"20":
        print("\n Surrender Your Luggage to Luggage comportment")

def SealCheking():
    print("\nSeal Checking Process")
    covid=input("\nYour Covid result is Positive or Negative: ")
    if covid=="negative":
        res = input("\nPlease Enter Your Passport Number: ")
        print("\nYour Seal Checking process is Complete, You Can go now to Boarding Place")
    elif covid=="positive":
        print("\nYou are Not eligible to travel, Because Your a Covid Attacked Person")
    else:
        print("\nInvalid Details, Try Again")

dept=input("Enter Your Departure Airport: ")
landing=input("Enter Your Landing Place: ")
print("Ticket prices")
print("\n1. Business Class = $600")
print("\n2. 1st Class = $400")
print("\n3. 2nd Class = $250")
ticket=input("\nSelect your Class : ")

if ticket=="1":
    print("\n You are Booked Business Class Ticket")
elif ticket=="2":
    print("\nYou are Booked 1st Class Ticket")
elif ticket=="3":
    print("\nYou are Booked 2nd Class Ticket")
else:
    print("\nInvalid Choice/, Try Again")

print("\nID Verification")
print("\nAadhar")
print("\nPAN")
print("\nVoter-ID")
id=input("\n Select YOur Given Proof Details ")
proofNO=input("\nEnter Your id proof card Number: ")
passportVerification()
covid()
Immigration()
Luggage()
SealCheking()