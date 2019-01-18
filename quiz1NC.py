#QuizNC.py
from quizNCvardef import *

global SCORE

def run_quest(quest, ansU, check, ansR):
    while check == False: #while the question hasn't been answered
        try:
            ansU = int(input(quest)) #ask the question
            print("")
            if ansU == ansR: #if the user gets the right answer
                print("Got it. Move on to the next question!")
                print("")
                global SCORE
                SCORE += 1
                check = True #change the state of the question. make it true

            elif 0 < ansU < 5: #if the answer is one of the choices but wrong
                print("Got it. Move on to the next question!")
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
run_quest(q3, ansU, check, q3CorAns)
run_quest(q4, ansU, check, q4CorAns)
run_quest(q5, ansU, check, q5CorAns)
run_quest(q6, ansU, check, q6CorAns)
run_quest(q7, ansU, check, q7CorAns)
run_quest(q8, ansU, check, q8CorAns)
run_quest(q9, ansU, check, q9CorAns)
run_quest(q10, ansU, check, q10CorAns)

print("score: ", SCORE * 10)
