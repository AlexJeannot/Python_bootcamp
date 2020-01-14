import random

def main():

    nb = random.randint(1, 99)
    cmp = 0

    while 1:
        user_nb = input("What's your guess between 1 and 99?\n>> ")
        try:
            user_nb = int(user_nb)
            if user_nb > 0 and user_nb < 100:
                if (nb == user_nb):
                    if (nb == 42):
                        print("The answer to the ultimate question of life, the universe and everything is 42.")
                    if (cmp == 0):
                        print("Congratulations! You got it on your first try!")
                    else:
                        print("Congratulations, you've got it!")
                    return 0
                elif (user_nb > nb):
                    print("Too high!")
                    cmp += 1
                else:
                    print("Too low!")
                    cmp += 1
            elif user_nb > 99:
                print("Put a number under 100")
            elif user_nb < 1:
                print("Put a number above 0")
        except:
            print("That's not a number")

main()
