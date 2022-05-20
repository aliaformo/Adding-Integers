
print("Welcome to this Adding Integers program")

adding_integers = True

while adding_integers: 
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")

    try:
        first_number = int(first_number)
        second_number = int(second_number)
        addition = first_number + second_number

        print(f"First number {first_number} + Second number {second_number} is equal to {addition}")

    except:
        print("You should enter an integer number in each input")
    
    cont_decision = input("Would you like to add another pair of integers? [y,n]: ")
    if cont_decision == "y":
        pass
    if cont_decision == "n":
        adding_integers = False
print("Thanks for using this Adding Integers program")

