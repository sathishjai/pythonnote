def getusernamepassword(username,password):
    if username!='abcd':
        print("incorrect username")
        username=input("username :")
        password=input("password :")
        getusernamepassword(username,password)
    elif password!='abcd':
        print("incorrect password")
username=input("username :")
password=input("password :")
getusernamepassword(username,password)
