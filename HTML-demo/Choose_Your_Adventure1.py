name = input("Type your name: ")
print("Welcome ", name ," to this Adventure Trip")

print("Let's start your Trip")

answer=input("You are in a forest and you lost a way to the road,after sometime you reached a Y junction,which way you want to go(left/right) " ).lower()

if answer == "left": 
    answer = input("you reached river, you have to swim across the river or walk around the river (swim/walk)").lower()

    if answer == "swim":
        print("you cought by crocodile, and you die")
    elif answer == "walk":
        print("you walk around the river ,you reached Tiger bone.....you caught by tiger , You Die")
    else:
        print("Not a valid Option..You loose")
elif answer == "right":
    answer = input("You reached a old house and a stranger sitting there..you have 2 options talk with stranger or kill that starnger(kill/talk) ").lower()

    if answer == "kill":
        print("Stranger guy died..you never find the road and you die in the Forest")
    elif answer == "talk":
        print("Starnger guy knows the way...he will guide you find road...you reached home...you survive")
    else:
        print("Not a valid Option...You loose")
else:
    print("Not a valid option..You loose")

print("Thanks for being with us", name)