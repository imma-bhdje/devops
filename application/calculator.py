import sys

while True:
    # take input from the command line arguments
    try:
        choice = int(sys.argv[1])
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid input.")
        break

    # check if choice is one of the four options
    if choice in (1, 2, 3, 4):
        if choice == 1:
            print("Sum : {} + {} = {}".format(num1,num2,num1+ num2))
            break

        elif choice == 2:
            print("Substraction : {} - {} = {}".format(num1,num2, num1- num2))
            break
        elif choice == 3:
            print("Multiplication : {} x {} = {}".format(num1,num2,num1*num2))
            break
        elif choice == 4:
            if (num2 == 0):
                print("Cannot divide by 0")
                break
            else :
                print("DIvision : {} / {} = {}".format(num1,num2, num1/num2))
                break
        print("To perform another calculation, please re-run the program with new arguments.")
    else:
        print("Invalid Input")
