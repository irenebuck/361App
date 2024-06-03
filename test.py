with open("usage.txt", "r") as file:
    print ({"count": len(set(file.read().splitlines()))})