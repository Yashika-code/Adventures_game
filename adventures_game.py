name=input("enter your name : ")
way=input(("here you  are on a long highway , there is two path of right and left : which one you want to choose : (left/right) : "))
if way == "right" :
    right=input("there is a river , by through this you want to across it with swim or walk : ")
    if right == "swim":
        print("in the river there are many crocodile . you lose!!")
    elif right=="walk":
        print("you by walk go through a mile away this is away from goal . you lose !!")
    else :
        print("invalid choice!")

if way=="left":
    left=input("there is a bridge , there is a man , you want to meet him or you want to cross it (cross/man) : ")
    if left == "cross":
        print("oh! you crossed the bridge and you lose!")
    elif left == "man":
        print("oh! you choose man , man give you a mistery box and you win !!")
    else :
        print("invalid choice!")

print(f"Thank you {name} for playing this adventures game!!")