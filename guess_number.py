import random 

try:
    low =int(input("enter lower side of num :"))
    high =int(input("enter higher side of num :"))
    a =random.randint(low,high) 
except:
    print('please enter valid number')


run =True

while(run):
    
    user_pick=int(input("enter num you want :"))
    if user_pick>low and user_pick<high:
        if a ==user_pick:
            print(f"your guess is right and number is : {a}")
            run =False
        elif a>user_pick:
            print(f"your num are lower than pc number")
        elif a<user_pick:
            print(f"your number bigger than pc number ")
    else:
        print(f'enter nubmer between {low} and {high}')