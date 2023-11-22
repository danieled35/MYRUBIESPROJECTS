# Assignment: Calculate Total Shopping Cart Cost
# 1. Create a Python function called calculate_item_cost that takes the price and quantity of an item as parameters. This function should return the total cost for that item, calculated as total_cost = price * quantity.



# Blessing  to  Everyone 2:45 PM
# 2. Create another Python function called calculate_total_cost that takes a list of items, where each item is represented as a tuple of (price, quantity). This function should also take the tax rate (as a decimal) and a discount rate (as a decimal) as parameters. The function should calculate and return the total cost of all items in the shopping cart, including tax and applying the discount if applicable.
# 3. Prompt the user to enter items into the shopping cart, including the price, quantity, tax rate, and discount rate, using the input() function.



# Blessing 2:46 PM
# 4. Use the calculate_item_cost function to calculate the cost of each item in the shopping cart.
# 5. Then, use the calculate_total_cost function to calculate the total cost of the shopping cart, including tax and discount.
# 6. Print the results, including the cost of each item and the total cost of the shopping cart.








# 1. Create Functions:

# Create a Python function called calculate_item_cost that takes the price and quantity of an item as parameters. This function should return the total cost for that item, calculated as total_cost = price * quantity.

# Create another Python function called calculate_total_cost that takes a list of items, a tax rate (as a decimal), and a discount rate (as a decimal) as parameters. This function should calculate and return the total cost of all items in the shopping cart, including tax and applying the discount if applicable.


# 2.User Input:

# Prompt the user to enter the number of items in the shopping cart.

# For each item, prompt the user to enter the price and quantity.

# Prompt the user to enter the tax rate (as a decimal, e.g., 0.08 for 8%).

# Prompt the user to enter the discount rate (as a decimal, e.g., 0.1 for 10%).

# 3.Calculate Item Costs:

# Use the calculate_item_cost function to calculate the cost of each item in the shopping cart.

# Store these costs in a list.
# 4. Calculate Total Cost:
# Use the calculate_total_cost function to calculate the total cost of the shopping cart. This should include tax and apply the discount if provided.


# 5.Display Results:

# Print the cost of each item in the shopping cart.

# Print the total cost of the shopping cart, including tax and the discount (if any).







def calculate_item_cost(price,quantity):
    total_cost = price * quantity
    return(total_cost)
def calculate_total_cost(items,tax_rate,discount_rate):
    total_cost=0
    for x in items:
        price,quantity=x
        item_cost=calculate_item_cost(price,quantity)
        total_cost+=item_cost
    total_cost_with_tax=total_cost*(1+tax_rate)
    total_cost_with_discount=total_cost_with_tax*(1-discount_rate)
    return(total_cost_with_discount)
items=[]
shopping_list=input("Enter your items ")
price=input("Enter the price of your items ")
quantity=input("Enter the quantity of your items ") 
discount_rate=input("please enter your discount rate ")
tax_rate=input("please enter your tax rate ")

    
