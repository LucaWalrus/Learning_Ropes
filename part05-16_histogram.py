def histogram(input_string):
    # Dictionary to store counts of each letter
    letter_counts = {}
    
    # Count occurrences of each letter
    for letter in input_string:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    # Print the histogram
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter} {'*' * count}")
