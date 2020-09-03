import re
x=True
while x:
    passw = input("entr password")
    if len(passw)<8 or len(passw)>15:
        print("INVALID PASSWORD")
        print("length of the password not less than 8 or not greater than 15 characters")
    elif not re.search("[a-z]",passw):
        print("INVALID PASSWORD")
        print("password must contain atleast 1 lower case letter")
    elif not re.search("[A-Z]",passw):
        print("INVALID PASSWORD")
        print("password must contain atleast 1 upper case letter")
    elif not re.search("[0-9]",passw):
        print("INVALID PASSWORD")
        print("passworrd must contain atlear 1 digit")
    elif not re.search("\W",passw):
        print("INVALID PASSWORD")
        print("password must contain atleast 1 nonword character")
    elif re.search("\s",passw):
        print("INVALID PASSWORD")
        print("password should not contain whitespacces")
    else:
        print("valid passsword")
