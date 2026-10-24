username = input("Enter your username: ").strip()
password = input("Enter your password: ")

# Username validation
username_valid = (
    5 <= len(username) <= 15
    and username.isalnum()
    and username[0].isalpha()
)

# Password validation
password_valid = (
    len(password) >= 8
    and any(char.isupper() for char in password)
    and any(char.islower() for char in password)
    and any(char.isdigit() for char in password)
    and any(char in "!@#$%^&*()/" for char in password)
    and " " not in password
)

if username_valid:
    print("Valid Username.")
else:
    print("""Invalid Username:
        - Must be between 5 and 15 characters.
        - Must start with a letter.""")

if password_valid:
    print("Password is valid.")
else:
   print("""
Invalid Password:
- Must be at least 8 characters.
- Must contain an uppercase letter.
- Must contain a lowercase letter.
- Must contain a number.
- Must contain a special character.
- Must not contain spaces.
""")