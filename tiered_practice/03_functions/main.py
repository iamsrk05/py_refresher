# def greet(name):
#     print("Hello", name)

# greet("bob")


# def add(name, age):
#     print (name, age)

# add("Kamla",23)

# def add(a, b):
#     return a + b

# result = add(5, 3)

# print(result)


# def check_even(number):
#     if number % 2 == 0:
#         return "Even Number"
#     else:
#         return "Odd Number"
        
# result = check_even(7)
# print(result)

code = 200
name = "Sam"

match code:
    case 200:
        print(f"Welcome {name}")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")




