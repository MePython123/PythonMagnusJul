user = input("Enter the Username: ")
password = input("Enter the Password: ")

if user=='python':
    if password=='welcome':
        print("Login Success")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")