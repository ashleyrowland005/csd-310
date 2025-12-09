# Function to calculate the square of a number
print("Debug: Starting program...")

def square(number):
    print("Debug: User entered:", value)    
    """
    Returns the square of the given number.
    :param number: int or float
    :return: int or float
    """
    # Input validation
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be an integer or float.")
    
    return number ** 2

# Main program
if __name__ == "__main__":
    try:
        # Get user input
        value = float((input("Enter a number: "))
        print("Debug: Function returned:", result)

        # Call the function and display the result
        result = square(value)
        print(f"The square of {value} is {result}")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except TypeError as e:
        print(e)
