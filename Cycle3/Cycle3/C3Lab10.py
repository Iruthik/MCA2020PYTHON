# Factors of a number

num = int(input("Enter a number:"))
count =  1
while count <= num:
    if num % count == 0:
        print(count)
    count = count + 1