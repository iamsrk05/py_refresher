
password = input("Enter your password(minimum 8 char + must contain mixed alphabet and special characters): ")

length_ok = len(password) >= 8
has_num = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()/" for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)


if length_ok and has_special and has_lower and has_num and has_upper:
    print("strong password")
else:
    print("Weak pass nigga. change it to save your ass..")
