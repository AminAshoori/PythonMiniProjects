import random
import time

def question_generator():
    a =random.randint(1,9)
    b =random.randint(1,9)
    
    operator =["+","-","*",]
    selected_operator = random.choice(operator)
    
    print(f"{a} {selected_operator} {b} = ?")
    
    if selected_operator == "+":
         return a+b
    elif selected_operator == "-":
         return a-b
    elif selected_operator == "*":
         return a*b



question_number_limit = 5
question_number = 0
score = 0
time_limit = 5


while question_number < question_number_limit :
    resault = str(question_generator())
    start_time =time.time()

    user_answer = input("enter your answer : ")
    end_time=time.time()
    
    
    time_diff=end_time-start_time
    
    if time_diff<time_limit:
        if resault ==user_answer:
            score +=1
            print(f"perfect, score is : {score}")
        else:
            print("sorry ,your answer is wrong")
    else:
        print('you are too late')
    
    question_number+=1
    
    