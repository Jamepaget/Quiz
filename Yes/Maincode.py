#functions

def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    questions = {
    "What is 5*3?: ":  "A",
    "What is 10*2?:":  "B",
    "What is 2*2?: ":  "A",
    "What is 20*2?:":  "C",
    "What is 4*3?:":   "A",
    "What is 5*5:":    "C",
    "What is 10*3:":   "A",
    "What is 8*4:":    "B",
    "What is 4*9:":    "B"
}

    for key in questions:
        print(key)
def check_answer():
    pass
def display_score():
    pass
def play_again():


options = [["A. 15", "B. 20", "C. 10"],
           ["A. 15", "B. 20", "C. 21"],
           ["A. 4", "B. 2", "C. 3"],
           ["A. 30", "B. 45", "C. 40"],
           ["A. 60", "B. 64", "C. 46"],
           ["A. 12", "B. 11", "C. 13"],
           ["A. 20", "B. 30", "C. 25"],
           ["A. 20", "B. 22", "C. 10"],
           ["A. 20", "B. 32", "C. 25"],
           ["A. 28", "B. 36", "C. 22"]]

# *** main routine
new_game()









