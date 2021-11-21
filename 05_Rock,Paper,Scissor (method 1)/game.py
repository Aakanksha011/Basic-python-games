import random

def gameWin(comp,you):

#Tie condition for both the side if they choose the same choice.
    if comp==you:
        return None

#All possibilties when the computer chosses rock(r)
    elif comp=='r':
        if you=='p':
            return True
        if you=='s':
            return False

##All possibilties when the computer chosses paper(p)
    elif comp =='p':
        if you =='s':
            return True
        if you=='r':
            return False

#All possibilties when the computer chosses scissor(s)
    elif comp =='s':
        if you=='r':
            return True
        if you=='p':
            return False

print("Computer's turn:Rock(r),paper(p) or scissor(s)?")

#assigning values to the random integer
randNo=random.randint(1,3)
if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='s'

you = input("your turn:Rock(r),paper(p) or scissor(s)?")

#storing thee function in a container
a = gameWin(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

#displaying of the results
if a == None:
    print("It was a tie!")
elif a == True:
    print("You win!")
else:
    print("You lose!")


    
