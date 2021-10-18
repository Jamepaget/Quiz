# Functions go here
def yes_no (questions):
    vaild = False
    while not vaild:
        response = input(questions).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no ")

# Instructions
def instructions():
    print("**** How to play ****")
    print()
    print("Have to answer with A,B,C to get a point. Do not type what ever the answer is or you will get it wrong ")
    print()
    return ""


# *** Main Routine ***

show_instructions = yes_no("Have you played the game before?")

if show_instructions == "no":
    instructions()


print("program continues")
