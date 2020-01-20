from book import Book
from recipe import Recipe
from datetime import datetime
import time

my_book = Book("Mon livre", datetime.now(), datetime.now(), [])


print("\n---- PRINT INSTANCE BOOK ----\n")
print(my_book)

print("\n---- PRINT ATTR INSTANCE BOOK ----\n")
print(my_book.name)
print(my_book.last_update)
print(my_book.creation_date)
print(my_book.recipes_list)


print("\n---- ADD FIRST RECIPE ----\n")
cake = my_book.add_recipe("cake", 1, 15, ["chocolate", "flour"], "a chocolate cake", "dessert")
print("UPDATE AFTER CAKE = {0}".format(my_book.last_update))
time.sleep(1.0)

print("\n---- PRINT INSTANCE RECIPE ----\n")
print(cake)

print("\n---- PRINT ATTR INSTANCE RECIPE ----\n")
print(cake.cooking_lvl)
print(cake.cooking_time)
print(cake.ingredients)
print(cake.description)
print(cake.recipe_type)


print("\n---- ADD SECOND RECIPE ----\n")
apple_pie = my_book.add_recipe("apple pie", 2, 25, ["apple", "honey"], "a apple pie", "dessert")
print("UPDATE AFTER APPLE PIE = {0}".format(my_book.last_update))

print("\n---- PRINT INSTANCE get_recipe_by_name ----\n")
my_book.get_recipe_by_name(cake)


print("\n---- PRINT INSTANCE get_recipes_by_types ----\n")
my_book.get_recipes_by_types("dessert")


print("\n---- PRINT INSTANCE ERROR get_recipe_by_name ----\n")
i = 1
my_book.get_recipe_by_name(i)
