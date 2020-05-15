#validates user input 0-4, no other input allowed
#module 2
def inputNumber(unsure_input):
    while True:
        try:
            userInput=int(input(unsure_input))
        except ValueError:
            print("\nNot an integer! Try again.\n")
            continue
        else:
            return emo_range(user_input)




def emo_range(unsure_input):
    while True:
        try:
            0 >= unsure_input <=4
        except ValueError:
            print("Not in range Try again.\n")
        else:
            return unsure_input
