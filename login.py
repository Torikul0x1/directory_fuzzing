name = input("Enter your name : ")
print("="*15 + " Welcome To the User Logged In Program " + name + " " + "="*15 + "\n")

while True:
    username = input("Enter your usernamme : ")
    password = input("Enter your password : ")
    if username == "Torikul0x1" and password == "TORIKUL12345":
        print("Successfully Logged IN!!")
        break
    else:
        print("Logged Failed!!")
        break