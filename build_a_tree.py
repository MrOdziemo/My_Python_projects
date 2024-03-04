answer = input("Enter number branch have a tree: ")
answer_number = int(answer)

branch = input("Enter what a symbol have a branch: ")

x = branch
y = " "
help_x = answer_number
help_y = 1

print((help_x + 1) * y, x)
for object in range(answer_number):
    print(help_x * y, help_y * x + x + x * help_y)
    help_x -= 1
    help_y += 1