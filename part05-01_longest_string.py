# Write your solution here
def longest(strings: list):
    initial_value = 0
    for item in strings:
        if len(item) > initial_value:
            initial_value = len(item)
            printout = item
        else:
            comp = len(item)
    return(printout)



if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
