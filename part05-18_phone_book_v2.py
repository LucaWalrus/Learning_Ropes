# Write your solution here
phone_book = {}

while True:  # Start an infinite loop, we'll break based on user input
    operation = int(input('command (1 search, 2 add, 3 quit): '))

    if operation == 1:  # Search operation
        name = input('name: ')
        if name in phone_book:  # Check if the name exists in the phone book
            print(', '.join(phone_book[name]))
        else:
            print('no number')

    elif operation == 2:  # Add operation
        name = input('name: ')
        number = input('number: ')
        if name in phone_book:  # If name exists, append the number to the list
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]  # Create a new list if the name doesn't exist
        print('ok!')
    
    elif operation == 3:  # Quit operation
        print('quitting...')
        break  # Exit the loop
