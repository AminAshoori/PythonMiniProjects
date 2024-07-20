from cryptography.fernet import Fernet



key =Fernet.generate_key()
encrypt =Fernet(key)

def add_pass(username,password):
    with open("./password.txt","a") as f:
        encrypted_pass =Fernet.encrypt(password)
        f.write(f"{username}-{password}\n")
    print("added.....")

def view_pass():
    with open("./password.txt","r") as f:
        for item in f:
            item =item.rstrip()
            username ,password = item.split("-")
            print(f"username : {username} and password : {password}")


while True:
    user_input = input("Enter the mode (v:view, a:add ,q:quit) : ")
    
    if user_input == "v":
        print("your password are as follows:")
        view_pass()
    elif user_input == "a":
        print("lets add user and pass:")
        
        username =input("enter your username : ")
        password =input("enter your password : ")
        
        add_pass(username,password)
    elif user_input=="q":
        break
    else:
        print("wrong input")