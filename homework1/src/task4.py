# Define a function that calculates the discounted price using a price and a discount amount
def calculate_discount(price, discount):

    # Check to make sure the arguments are of the correct type (integer/float)
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        
        # If they are not the right data types, tell the user
        raise TypeError("Price and discount must be numeric.")
    
    # Check to make sure the price is positive
    if price < 0:

        # If the price is negative, tell the user
        raise ValueError("Price cannot be negative.")

    # Check to see if the discount is valid (between 0 and 100 percent)
    if not (0 <= discount <= 100):

        # If the discount is not valid tell the user
        raise ValueError("Discount must be between 0 and 100 percent.")

    # Return the calculated discounted price
    return price - (price * (discount / 100))