spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_list = [food["name"] for food in spicy_foods]
    return food_list
    pass

def get_spiciest_foods(spicy_foods):
    spicy_list = [food for food in spicy_foods if food["heat_level"]>5]
    return spicy_list
    pass
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine: 
            return food
    pass

def print_spiciest_foods(spicy_foods):
    spicy_list = [food for food in spicy_foods if food["heat_level"]>5]            
    print_spicy_foods(spicy_list)
    

def get_average_heat_level(spicy_foods):
    total_heat= sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat/len(spicy_foods)
    return int(average_heat)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
