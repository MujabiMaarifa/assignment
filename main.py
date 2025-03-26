"""
Create a function named calculate_discount(price, discount_percent)
that calculates the final price after applying a discount.
The function should take the original price (price)
and the discount percentage (discount_percent) as parameters.
If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item
and the discount percentage. Print the final price after applying the discount,
or if no discount was applied, print the original price.
"""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        discount = price * (discount_percent/100)
        print("The discount allowed is: ", discount)
        finalPrice = price - discount
        return finalPrice
    else :
        print("Discount percent is below the required percentage for discount to be allowed!!")
        return price

print("Lets calculate prices based on discounts |_| ..enjoy\n")
p = float(input("Enter the price of an item: "))
d = int(input("Enter the percentage discount in (%): "))
print("The original price is: ", p)
print("The discount made on the item is: ", d , "%")
final_price = calculate_discount(p, d)
print("The final price is: ", final_price)
