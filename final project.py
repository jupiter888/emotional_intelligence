from emoci import *
def mainMenu():
    print("Welcome to the Gallery of Emotions\n")
    while True:
        try:
            startChoice = int(input("1 to enter Gallery of emotions, 0 to quit"))
            if startChoice == 1:
                print("~~~~Welcome to the Gallery of Emotions~~~~\n")
                continue_onward("start exploring")
                begin()  # prints intro to emotions
                continue_onward("understand your feeling")
                understand(feel())  # how you feeling?->outer function explains emotion
                continue_onward("see the causes")
                cause()
                continue_onward("see the responses")
                response(trigger())# response(feeling #)->print dict responses,choose->pass int to response explained.
                continue_onward("see emotional hygiene techniques")
                strategy()# strategies()->prints list of healthy coping->any key to start over
                break
            elif startChoice == 0:
                print(startChoice + "entered, Session End.\n")
                break
            else:
                print(startChoice + " entered, option unavailable.\n")
                mainMenu()
        except ValueError:
            print(startChoice + " entered, Input invalid. Session End")
    exit


# main
mainMenu()
