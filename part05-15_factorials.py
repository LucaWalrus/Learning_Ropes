# Write your solution here
def factorials(n: int):
    k = {}  # Initialize an empty dictionary
    i = 1  # Start from 1
    while i <= n:  # Loop up to and including n
        result = 1  # Reset result for each new factorial
        j = i  # Temporary variable to calculate factorial
        while j > 0:  # Calculate factorial of i
            result *= j
            j -= 1
        k[i] = result  # Store the result in the dictionary
        i += 1  # Move to the next number
    return k  # Return the dictionary
