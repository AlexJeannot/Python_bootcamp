
def add_recipe(cookbook):
    name = raw_input("Please name the recipe\nYour choice : \n")

    add = True
    ingredients_list = []
    while add == True:
        ingredient = raw_input("Please add ingredient. If you have finish write exit\nYour choice : ")
        if ingredient == "exit":
            add = False
        else:
            ingredients_list.append(ingredient)

    meal = raw_input("What kind of meal is it ?\nYour choice : \n")

    prep = True
    while prep == True:
        time = raw_input("How much time do you need to make this recipe ?\nYour choice : ")
        try:
            time = int(time)
            prep = False
        except:
            print("That's not a number")
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients_list
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = time
    return cookbook

def delete_recipe(cookbook):
    suppr = True

    while suppr == True:
        name = raw_input("Which recipe do you want to delete ?\nYour choice : ")
        try:
            del cookbook[name]
            suppr = False
        except:
            print("This recipe doesn't exist")
    return cookbook

def print_recipe(cookbook):
    display = True

    while display == True:
        name = raw_input("Which recipe do you want to display ?\nYour choice : ")
        try:
            print("Recipe for {0}:\nIngredients list: {1}\nTo be eaten for {2}.\nTakes {3} minutes of cooking.\n\n".format(name, cookbook[name]["ingredients"], cookbook[name]["meal"], cookbook[name]["prep_time"]))
            display = False
        except:
            print("This recipe doesn't exist")
    return 0

def print_cookbook(cookbook):

    for elem in cookbook:
        print("Recipe for {0}:\nIngredients list: {1}\nTo be eaten for {2}.\nTakes {3} minutes of cooking.\n\n".format(elem, cookbook[elem]["ingredients"], cookbook[elem]["meal"], cookbook[elem]["prep_time"]))
    return 0

def main():
    boucle = True
    cookbook =  {
                    "sandwich" : {"ingredients": ["ham", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10},
                    "cake" : {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
                    "salad" : {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}
                }
    while boucle == True:
        choice = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n\nYour choice : ")
        if choice == 1:
            cookbook = add_recipe(cookbook)
        elif choice == 2:
            cookbook = delete_recipe(cookbook)
        elif choice == 3:
            cookbook = print_recipe(cookbook)
        elif choice == 4:
            cookbook = print_cookbook(cookbook)
        elif  choice == 5:
            boucle = False
        else:
            print("Incorrect choice")
    return 0

main()
