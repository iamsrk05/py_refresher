# Tier 1 - Problem 4: Dictionary practice
#
# Start with this dictionary, then complete each exercise below.

account = {
    "username": "sam22",
    "email": "sam@email.com",
    "status": "inactive",
    "login_attempts": 3,
}


# 1. Change "status" from "inactive" to "active" using normal dictionary
#    assignment.

account["status"] = "active"
print(account)

# 2. Use .update() to change "login_attempts" to 0 and add:
#    "verified": True

account.update({
    "login_attempts": 0,
    "verified": True
})
print(account)



# 3. Remove "email" using .pop() and store the removed value in a variable
#    called removed_email.

removed_email = account.pop("email")

# 4. Print removed_email.
print(f"The removed email is: {removed_email}")

# 5. Print the final dictionary.

print(account)
# 6. Explain: Why can .pop() both remove "email" from the dictionary and put
#    its old value into removed_email?
#
# Answer: Because pop took the variable name and took out the value of the variable and put it down to a new assigned variable named removed_email.
#
# account.pop("email")
#         ↓
# 1. Finds the key "email"
# 2. Removes that key-value pair from account
# 3. Returns the removed VALUE
#         ↓
# "sam@email.com"
#         ↓
# 4. = stores that returned value in removed_email
#
# Interview-ready explanation
# .pop("email") removes the "email" key-value pair and returns its value. Because that returned value is assigned to removed_email, the variable stores the removed email address.
