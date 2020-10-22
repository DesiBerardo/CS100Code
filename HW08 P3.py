'''
Desimir Berardo
CS100 113
10/22/2020
'''

def enterNewPassword():
    passLoop = False
    while True:
        password = input("Enter a password between 8-15 characters including at least 1 digit: ")
        if len(password) < 8 or len(password) > 15:
            print("Password must be between 8-15 characters!")
            continue
        for i in password:
            if i.isdigit():
                passLoop = True
        if passLoop == False:
            print('Password must have a digit!')
        else:
            print('password accepted')
            break


enterNewPassword()