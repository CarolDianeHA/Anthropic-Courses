def greeting():
    print("Hi there")


def calculate_pi_to_5th_digit():
    """
    Calculate pi to the 5th decimal digit using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Returns:
        float: Pi calculated to at least 5 decimal places (3.14159)
    """
    def arctan(x, num_terms=100):
        """
        Calculate arctan(x) using Taylor series expansion.
        arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
        """
        result = 0
        for n in range(num_terms):
            sign = (-1) ** n
            term = sign * (x ** (2 * n + 1)) / (2 * n + 1)
            result += term
        return result
    
    # Using Machin's formula for better convergence
    pi = 4 * (4 * arctan(1/5) - arctan(1/239))
    
    # Round to 5 decimal places
    return round(pi, 5)