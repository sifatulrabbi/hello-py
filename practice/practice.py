# some basics of pythons

person_name = "John"
person_age = 70

name = input("Enter your name: ")

print(
    f"Hey {name}, let me tell you a story\n"
    f"There once was a man called {person_name}, he was 70 years old.\n"
    f"He really liked the name John but didn't like being {person_age}"
)

# lists / array in python

fav_foods = ["chicken", "beef", "lamb", "milk", "fruit"]

recipes = ["pudding", "burger"]

fav_foods.append("pizza")
fav_foods.remove("lamb")
fav_foods.insert(4, "pasta")
fav_foods.pop()

foods = fav_foods.copy()
foods.extend(recipes)

print(f"fav foods: {fav_foods}")
print(f"recipes: {foods}")

# tuples

person_tuple = ("Sifatul", {})
coordinates = (4, 5)


def say_hello(_name):
    print(f"hello I'm  {_name}")


say_hello(person_tuple[0])

# if else statements

is_raining = False
is_in_mode = not is_raining
is_hungry = True

if is_raining and not is_hungry:
    print("I'm sleeping and not in mode")

elif is_hungry and not is_raining:
    print("I'm hungry and not in mode")

else:
    print("I'm not sleeping")

if is_in_mode:
    print("I'll play game")

else:
    print("I'll not play game")

my_dictionary = {"name": "Temujin", "age": "20", "loves": "programming"}

print(my_dictionary["name"])

if int(my_dictionary["age"]) < 18:
    print("You cant view this content")
else:
    print("You are allowed to view this content")


# finding duplicates in an array

arr_num = [5, 7, 1, 2, 4, 7, 4]

for number in arr_num:
    arr_num.remove(number)

    if arr_num.__contains__(number):
        print(f"{number} has a duplicate")
