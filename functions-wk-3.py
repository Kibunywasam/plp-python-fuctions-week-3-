# Define a function to calculate the final price after discount
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

# Calling function and displaying output
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: ksh. {final_price}")
    else:
        print(f"No discount applied. Final price: ksh. {final_price}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
