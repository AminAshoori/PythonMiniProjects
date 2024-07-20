import random

names = ['amin','nima','mamad','hamid','armin','ahmad','ali','niosha']

selected_name = random.choice(names).lower()


guess_count = len(selected_name)
guessed_list =["-"]*len(selected_name)
current_guess =" ".join(guessed_list)
print(current_guess)


while guess_count > 0:
    guessed_char = input(' enter a char: \n')
    
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("you have guessed before,try again")
            else:
                for idx,char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                current_guess =" ".join(guessed_list)
                print(f"perfect => {current_guess} ")
                
                if not "-" in guessed_list:
                    print("you won")
                    break
        else:
       
            print(f'its wrong s')
    else:
        print("please enter a valid char")