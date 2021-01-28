input_string = input("Enter a list elements")
print("\n")
userList = input_string.split()
print("user list is ", userList)

sum = 0
for num in userList:
    sum += int(num)
print("Sum of given list = ", sum)