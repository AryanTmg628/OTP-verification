
'''
Create a 6-digit random number
Store it in a variable
SEnd it to the email
Ask for the OTP
IF it maches Verifres
Else Resend
'''

#importing the necessary modules
from random import choice,random
import smtplib
import math
from os import system


#defining the random number

def getRandomNumber(number) :

    #creating the variable 
    OTP = ""

    for i in range(6) :

        OTP += number[math.floor(random()*10)]
        continue
    
    #returning the 6-digit random code (OTP One time Password)
    return OTP

if __name__ == "__main__" :

    OTP = getRandomNumber("0123456789")

    #Activating the Simple Main Transfer Protocol

    s = smtplib.SMTP("smtp.gmail.com",587)

    #starting the Transport Layer Security
    s.starttls()

    #loginning in
    s.login("AryanTmg28@gmail.com","mvmh scit mucd dvon")

    #asking user for the email
    userEmail = input("\n"*3 + "\t"*5 + "Enter your e-mail : ")

    #sending the OTP message to the user email
    s.sendmail("AryanTmg28",userEmail,"{} is your OTP From ARYAN Tech Company".format(OTP))

    #asking the user for the otp to verify

    verificationOTP = input("\n"*2 + "\t" *5 + "Enter the OTP : ")

    #if verfication OTP and OTP matches

    if (verificationOTP == OTP) :

        print("Verified")

    else :

        print("Wrong!!!")