# Write your solution here

def oldest_person(people: list):
    check = people[0][1]
    for i in range(len(people)):
        if people[i][1] <= check:
            check = people[i][1]
            result = people[i][0]
    return result

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Daisy", 1892)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    p5 = ("Dunja", 1919)
    people = [p1, p2, p3, p4, p5]

    print(oldest_person(people))
