print("Lets SignUp!")

name = input("Enter your full-name: ")
user_name = input("Enter your prefered username: ").strip().lower()
user_pass = input("Enter your prefered password: ").strip()
account = {
    "name" : name,
    "username" : user_name,
    "password" : user_pass
}
    
    












# saved_username = "admin1"
# saved_password = "admin123@"

# entered_username = input("enter your username: ").strip().lower()
# entered_password = input("enter your password: ").strip()

# if entered_username == saved_username:
#     if entered_password == saved_password:
#         print(f"Login successful. Welcome back, {saved_username}!")
#     else:
#         print("Incorrect password. Access denied.")
# else:
#     print("Username not found. Access denied.")