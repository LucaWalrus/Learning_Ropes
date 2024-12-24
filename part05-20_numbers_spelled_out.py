# Write your solution here

def dict_of_numbers():
    # Define mappings for numbers 0-19, tens multiples (20, 30, ..., 90)
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    # Create an empty dictionary to store the numbers and their word equivalents
    number_dict = {}

    # Loop through numbers 0 to 99 and add the corresponding word
    for i in range(100):
        if i < 20:
            number_dict[i] = ones[i]  # For numbers 0-19, use the "ones" list
        else:
            tens_place = i // 10  # Get the tens place
            ones_place = i % 10   # Get the ones place
            if ones_place == 0:
                number_dict[i] = tens[tens_place]  # For multiples of 10 (20, 30, ..., 90)
            else:
                number_dict[i] = tens[tens_place] + '-' + ones[ones_place]  # For numbers like 21, 35, 88, etc.
    
    return number_dict
