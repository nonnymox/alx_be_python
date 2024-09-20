user_input = int(input("Enter the size of the pattern: "))
i = 0

while i < user_input:
    for j in range(user_input):
        print("*", end="")
    print()
    i += 1

# user_input = int(input("Enter the size of the pattern: "))
# for i in range(0, user_input):
#     print("*" * user_input)
