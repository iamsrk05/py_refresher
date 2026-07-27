name = input("Enter your name: ")
age = int(input("Enter your age: "))
movie_type = input("Enter your genre: ").lower()

adult_price = 24
child_price = adult_price / 2

ticket_type = ""
ticket_price = 0
discount_price = 0
final_price = 0

if movie_type == "horror":
    if age >= 18:
        ticket_type = "Adult Ticket"
        ticket_price = adult_price
        is_member = input("Enter if youre already a member(Yes/No): ").lower()    
        if is_member == "yes":
           discount_price = int(adult_price * 0.3)
           final_price = adult_price - discount_price
        else:
            final_price = ticket_price
    else:
        print("You're not allowed to watch this movie.")
else:
    if age < 5:
        ticket_type = "Free Ticket"
        ticket_price = 0
        final_price = 0

    elif age <= 17:
        ticket_type = "Child Ticket"
        ticket_price = child_price
        final_price = child_price
    else:
        ticket_type = "Adult Ticket"
        ticket_price = adult_price

        is_member = input("Enter if you're already a member(Yes/No): ").lower()

        if is_member == "yes":
            discount_price = int(ticket_price * 0.3)
            final_price = ticket_price - discount_price

        else:
            final_price = ticket_price  

print("=========================")
print("       MOVIE TICKET")
print("=========================")

print(f"Customer Name: {name}")
print(f"Age: {age}")
print(f"Movie Genre: {movie_type}")
print(f"Ticket Type: {ticket_type}")
print(f"Ticket Price: ${ticket_price}")
print(f"Discount: ${discount_price}")
print(f"Final Amount: ${final_price}")

print("=========================")
print("Thank you for booking!")
print("=========================")
