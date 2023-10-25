import sys
import logging

items = [
    {"name": "snus", "quantity": 100, "unit": "boxes", "unit_price": 15.99},
    {"name": "beer", "quantity": 500, "unit": "bottles", "unit_price": 2.49},
    {"name": "wine", "quantity": 200, "unit": "bottles", "unit_price": 12.99},
    {"name": "vodka", "quantity": 50, "unit": "bottles", "unit_price": 24.99},
]

def get_items():
    print("The list of available products in the warhouse:")
    for item in items:
        print(f"Item name: {item['name']}")
        print(f"Quantity of items: {item['quantity']} {item['unit']}")
        print(f"Unit price: {item['unit_price']} zł\n")

def add_item():
    print("Adding to warehouse...")
    name = input("Item name: ")
    unit_name = input("Unit name: ")
    quantity = int(input("Item quantity: "))
    unit_price = float(input("Unit price: "))  

    new_item = {
        "name": name,
        "unit": unit_name,
        "quantity": quantity,
        "unit_price": unit_price
    }

    items.append(new_item)
    print("Succesfully")


operation = input("What would you like to do?")
while operation != "exit":
    if operation == "show":
        get_items()
        break
    if operation == "add":
        add_item()
        break
else:
        print("Exiting...Bye!")

def add_item(name, unit_name, quantity, unit_price):
     print("Adding to warehouse...")
     

    