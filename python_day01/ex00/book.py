from recipe import Recipe
from datetime import datetime

class Book:

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        for elem in self.recipes_list:
            if name == elem:
                print(elem)
                return elem

    def get_recipes_by_types(self, recipe_type):
        for elem in self.recipes_list:
            if elem.recipe_type == recipe_type:
                print(elem)
                print("\n")
        return 0

    def add_recipe(self, recipe, cook_lvl, cook_time, ingredients_list, descrip, recipe_type):
#        cook_lvl = input("What is the cooking level ?\n>> ")
#        cook_time = input("What is the cooking time ?\n>> ")

#        ing = True
#        ingredients_list = []
#        while ing == True:
#            ingredient = raw_input("What are the ingredients ?\n>> ")
#            if ingredient == "exit":
#                ing = False
#            ingredients_list.append(ingredient)

#        descrip = raw_input("What is the description ?\n>> ")
#        recipe_type = raw_input("What is the recipe type ?\n>> ")

        obj = Recipe(recipe, cook_lvl, cook_time, ingredients_list, descrip, recipe_type)
        self.last_update = datetime.now()
        self.recipes_list.append(obj)
        return obj
