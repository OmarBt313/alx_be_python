size = int(input("Enter the size of the pattern:"))

i = 0

while i < size:
    for x in range(0, size):
        print("*", end="")
    print()
    i+=1

    