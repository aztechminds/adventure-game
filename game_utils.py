
# defination to solve the riddle
def solve_riddle(riddle):
    print(riddle['question'])
    user_answer = input("Your answer: ")

    if user_answer.lower() == riddle['answer'].lower():
        return True
    else:
        print("Wrong answer! Try again.")
        return False
    

def end_game():
    print("Thank you for playing this game! See you soon.")
    exit(0)
