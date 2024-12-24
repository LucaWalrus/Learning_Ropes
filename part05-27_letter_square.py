# Write your solution here
layers = int(input("Layers: "))

# Calculate the size of the square
size = 2 * layers - 1

# Loop through each row
for i in range(size):
    row = ""
    # Loop through each column in the row
    for j in range(size):
        # Find the minimum distance to any edge (top, bottom, left, right)
        distance_to_edge = min(i, j, size - i - 1, size - j - 1)
        
        # The letter for this position is determined by how far it is from the edge
        letter = chr(65 + layers - 1 - distance_to_edge)
        
        # Add the letter to the row
        row += letter
    
    # Print the row
    print(row)
