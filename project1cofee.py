menu = {
    'pizza': 40,
    'pasta': 30,
    'burger': 70,
    'cofee': 50,
}

print("Welcome to my Python restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: RS{price}")

order_total = 0

# First item
item_1 = input("Enter name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} added to your order")
else:
    print(f"Item {item_1} is not available yet!")

# Always ask for another item
another_order = input("Do you want to add another item? (yes/no): ").lower()
if another_order == 'yes':
    item_2 = input("Enter name of the second item you want to order: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} added to your order")
    else:
        print(f"Item {item_2} is not available")

print(f"The total amount to pay is RS{order_total}")




