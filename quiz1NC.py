#QuizNC.py

def run_quest(quest, ansU, check, ansR, grade):
    while quest == False: #while the question hasn't been answered
    try:
        ansU = int(input(quest)) #ask the question
        print("")
        if ansR == int(3): #if the user gets the right answer
            quest = True #change the state of the question. make it true
            grade += 1 #add to the score
            print("Correct.")
            print("Move on to the next question!")
        

        elif 0 < ansU < 5: #if the answer is one of the choices but wrong
            print("Sorry your answer is not correct. The answer was 3.\n")
            print("Please move on to the next question.")
            break #break the loop.

    except ValueError: #if they inputted anything else
        print("")
        print("Please put the number of the answer choice\n") #tell directions
  
    
q1 = bool(False)
score = int(0) # the score
q1ans = int(0) # the answer to user inputs
q1ask = str("""1. What is the most well-known coding language?\n
            1. Elixir
            2. Python
            3. JavaScript
            4. Swift\n""")
print("")
print("please only type the number of the answer choice you have chosen.")
print("")      

        
