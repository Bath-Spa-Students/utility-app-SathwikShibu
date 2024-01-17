print('''
░██████╗░█████╗░████████╗██╗░░██╗░██╗░░░░░░░██╗██╗██╗░░██╗██╗░██████╗
██╔════╝██╔══██╗╚══██╔══╝██║░░██║░██║░░██╗░░██║██║██║░██╔╝╚█║██╔════╝
╚█████╗░███████║░░░██║░░░███████║░╚██╗████╗██╔╝██║█████═╝░░╚╝╚█████╗░
░╚═══██╗██╔══██║░░░██║░░░██╔══██║░░████╔═████║░██║██╔═██╗░░░░░╚═══██╗
██████╔╝██║░░██║░░░██║░░░██║░░██║░░╚██╔╝░╚██╔╝░██║██║░╚██╗░░░██████╔╝
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═════╝░

██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝''')

# Vending machine items and prices
items = {
    '1': {'name': 'Oman Chips', 'price': 0.50},
    '2': {'name': 'Sohar Chips', 'price': 0.50},
    '3': {'name': 'Pepsi', 'price': 2.50},
    '4': {'name': 'Water', 'price': 1.00},
    '5': {'name': '7up', 'price': 2.50},
    '6': {'name': 'Sandwich', 'price': 3.00},
    '7': {'name': 'Diary Milk', 'price': 2.00},
    '8': {'name': 'Kitkat', 'price': 2.50},
    '9': {'name': 'Flakes', 'price': 2.50},
    '10': {'name': 'Twix', 'price': 1.50},
    '11': {'name': 'Skittles', 'price': 3.00},
    '12': {'name': 'm&m', 'price': 4.00}
}

# Display available items and prices
print('''
𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒕𝒉𝒆 𝑽𝒆𝒏𝒅𝒊𝒏𝒈 𝑴𝒂𝒄𝒉𝒊𝒏𝒆❗''')
print("Please select an item:")
for key, item in items.items():
    print(f"{key}. {item['name']} - dhs{item['price']}")

# Prompt user for input
selection = input("Enter the item number you wish to purchase: ")

# Check if the selected item is valid
if selection in items:
    selected_item = items[selection]
    print(f"You have selected {selected_item['name']}.")
    amount_due = selected_item['price']

    # Prompt user to insert money
    while amount_due > 0:
        try:
            payment = float(input(f"Please insert dhs{amount_due:.2f}: "))
            if payment >= amount_due:
                change = payment - amount_due
                print(f"Thank you for your purchase! Your change is dhs{change:.2f}.")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                amount_due -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")