Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # define the menu
... menu={
...     'pizza':50,
...     'pasta':50,
...     'burger':60,
...     'tea':20,
...     'coffee':80,
... 
... }
... print(menu)
... 
... # greeting
... print("welocme to Restaurant")
... print("pizza: Rs50\npasta: Rs50\nburger: Rs60\ntea:Rs20\ncoffee: Rs80\n")
... 
... order_total = 0
... 
... item_1 = input("Enter the name of the item =")
... if item_1 in menu:
...     order_total += menu[item_1]
...     print(f"your item{item_1} has been added to your order")
... else:
...     print(f"Ordered item {item_1} is not available yet!")
... 
... another_order = input("Do you like to add another item? (Yes/No) ")
... 
... if another_order == "yes":
...     item_2 = input("Enter the name of second item = ")
...     if item_2 in menu:
...         order_total += menu[item_2]
...         print(f"item {item_2} has been added to order")
...     else:
...         print(f"ordered item {item_2} is not available!")
... 
