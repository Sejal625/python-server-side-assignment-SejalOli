""" 7 Prase a JSON file representing product details(name,price,quantity)and display
the details in tabular format"""

import json

with open('product_details.json', 'r') as file:
    products = json.load(file)

print("{:<20} {:>10} {:>10}".format("Name", "Price", "Quantity"))
print("-" * 42)

for item in products:
    print("{:<20} {:>10.2f} {:>10}".format(item['Name'], item['Price'], item['Quantity']))