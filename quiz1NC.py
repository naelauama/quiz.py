#QuizNC.py
from quizNCvardef import *

def run_quest(quest, ansU, check, ansR):
    while check == False: #while the question hasn't been answered
        try:
            ansU = int(input(quest)) #ask the question
            print("")
            if ansU == ansR: #if the user gets the right answer
                print("Move on to the next question!")
                print("")
                check = True #change the state of the question. make it true

            elif 0 < ansU < 5: #if the answer is one of the choices but wrong
                print("Please move on to the next question.")
                print("")
                break #break the loop.
            else:
                print("Please put the number of one of the answer choice\n")

        except ValueError: #if they inputted anything else
            print("")
            print("That is not an acceptable answer!")
            print("Please put the number of the answer choice\n") #tell directions

run_quest(q1, ansU, check, q1CorAns)
run_quest(q2, ansU, check, q2CorAns)
