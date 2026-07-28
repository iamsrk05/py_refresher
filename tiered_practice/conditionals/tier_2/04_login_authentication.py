saved_username = "admin1"
saved_password = "admin123@"

entered_username = input("enter your username: ").strip().lower()
entered_password = input("enter your password: ").strip()

if entered_username == saved_username:
    if entered_password == saved_password:
        print(f"Login successful. Welcome back, {saved_username}!")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found. Access denied.")