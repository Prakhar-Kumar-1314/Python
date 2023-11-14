import random
start = input("Enter the start of the range: ")

while not start.isdigit():
    print("Please enter a valid number.")
    start = input("Enter the start of the range: ")

end = input("Enter the end of the range: ")

while not end.isdigit() or int(end) < int(start):
    print("Please enter a valid number.")
    if int(end) < int(start):
        print("End of the range should be greater than start of the range")
        end = input("Enter the end of the range: ")

random = random.randint(int(start), int(end))
print(random)
count = 1

while True:
    user_input = input("Guess the number: ")
    if not user_input.isdigit():
        print("Please enter a valid number.")
    if int(user_input) == random:
        break
    else:
        count += 1

if count > 1:
    x = "s"
else:
    x = ""

print(f"You guessed the number in {count} attempt{x}")
