def calculate_total_cost(item_prices):
    total_cost_before_tax=sum(item_prices)
    tax_rate=0.08
    tax_amount=tax_rate*total_cost_before_tax
    total_final_cost=tax_amount+total_cost_before_tax
    return(total_final_cost)
# print(calculate_total_cost([2,5,8]))

yes=[5,7,8,4,3,5,8,7]
total_cost=calculate_total_cost(yes)
print(total_cost)