# Product catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

# Function to calculate the total amount for a product
def calculate_product_amount(quantity, price, gift_wrap):
    product_amount = quantity * price
    if gift_wrap:
        product_amount += quantity  # Gift wrap fee is $1 per unit
    return product_amount

# Function to calculate the discount amount
def calculate_discount(total_quantity, product_quantity, price):
    discount_amount = 0
    for rule, (threshold, discount) in discount_rules.items():
        if total_quantity > threshold or product_quantity > threshold:
            if rule == "tiered_50_discount":
                quantity_above_threshold = max(product_quantity - threshold, 0)
                discount_amount += quantity_above_threshold * price * discount
            else:
                discount_amount += price * discount
    return discount_amount

# Function to calculate the shipping fee
def calculate_shipping_fee(total_quantity):
    return (total_quantity - 1) // 10 * 5

# Function to get user input
def get_user_input(product_name):
    quantity = int(input(f"Enter the quantity of {product_name}: "))
    gift_wrap = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"
    return quantity, gift_wrap

# Main program
subtotal = 0
total_quantity = 0
discount_amount = 0

for product_name, price in catalog.items():
    quantity, gift_wrap = get_user_input(product_name)
    product_amount = calculate_product_amount(quantity, price, gift_wrap)
    discount_amount += calculate_discount(total_quantity, quantity, price)
    
    subtotal += product_amount
    total_quantity += quantity

# Calculate shipping fee
shipping_fee = calculate_shipping_fee(total_quantity)

# Calculate total
total = subtotal - discount_amount + shipping_fee

# Output the details
# print("\n--- Order Details ---")
# for product_name, price in catalog.items():
#     quantity, _ = get_user_input(product_name)
#     product_amount = calculate_product_amount(quantity, price, False)
#     print(f"{product_name} - Quantity: {quantity} - Total: ${product_amount}")

print(f"\nSubtotal: ${subtotal}")
print("Discount applied: None")  # No discount applied for each product
print(f"Shipping fee: ${shipping_fee}")
print(f"Total: ${total}")
