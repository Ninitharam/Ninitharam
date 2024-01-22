from functools import reduce

# Final data structure

class IndianDish:
    def __init__(self, name, ingredients, spice_level, vegetarian):
        self.name = name
        self.ingredients = ingredients
        self.spice_level = spice_level
        self.vegetarian = vegetarian

    def __repr__(self):
        return f"{self.name} ({'Vegetarian' if self.vegetarian else 'Non-Vegetarian'}): {', '.join(self.ingredients)}, Spice Level: {self.spice_level}"

# Mostly side-effect-free function
    
def display_dish(dish):
    print(dish)

# Use higher-order function
    
def display_menu(menu, display_func):
    print("Indian Cuisine Menu:")
    for dish in menu:
        display_func(dish)
    print()

# Function as a parameter
    
def filter_vegetarian(menu):
    return list(filter(lambda x: x.vegetarian, menu))

# Use closures/anonymous functions

def spice_level_filter(level):
    return lambda x: x.spice_level == level

# Define initial data structure

biryani = IndianDish("Chicken Biryani", ["Basmati Rice", "Chicken", "Spices"], "High", False)
dal_tadka = IndianDish("Dal Tadka", ["Lentils", "Tomatoes", "Spices"], "Medium", True)
paneer_butter_masala = IndianDish("Paneer Butter Masala", ["Paneer", "Tomato Sauce", "Spices"], "Medium", True)
masala_dosa = IndianDish("Masala Dosa", ["Rice Batter", "Potato Filling", "Spices"], "Medium", True)

# Create a list of Indian dishes

indian_menu = [biryani, dal_tadka, paneer_butter_masala, masala_dosa]

# Display the menu using functional aspects

display_menu(indian_menu, display_dish)

# Using function as a parameter

vegetarian_dishes = filter_vegetarian(indian_menu)
display_menu(vegetarian_dishes, display_dish)

# Using closures/anonymous functions

medium_spice_filter = spice_level_filter("Medium")
medium_spice_dishes = list(filter(medium_spice_filter, indian_menu))
display_menu(medium_spice_dishes, display_dish)
