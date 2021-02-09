def pattern(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(i * j, end="   ")
        print("\n")
step=int(input("Enter the step number of pyramid:"))
pattern(step)