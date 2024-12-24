# Write your solution here

def create_tuple(x: int, y: int, z: int):
    sums = x + y + z
    if x < y and x < z:
        if y > z:
            return (x, y, sums)
        else:
            return (x, z, sums)
    elif y < x and y < z:
        if x > z:
            return (y, x, sums)
        else:
            return (y, z, sums)
    elif z < x and z < y:
        if x > y:
            return (z, x, sums)
        else:
            return (z, y, sums)
    
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))        
