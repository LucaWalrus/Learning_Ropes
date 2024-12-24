# Write your solution here

def invert(dictionary: dict):
    # Create a new dictionary to store the inverted key-value pairs
    inverted_dict = {v: k for k, v in dictionary.items()}
    
    # Clear the original dictionary and update it with the inverted values
    dictionary.clear()
    dictionary.update(inverted_dict)

# Example usage
#s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
#invert(s)
#print(s)
