def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Ask the user to input the price and discount
price = float(input("Original price: "))
discount = float(input("Discount percentage: "))

final_price = calculate_discount(price, discount)

if discount >= 20:
    print("Discount applied. Final price:", round(final_price, 2))
else:
    print("No discount applied. Final price:", round(final_price, 2))
