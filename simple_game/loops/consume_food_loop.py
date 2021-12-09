from simple_game.components.food_store import FoodStore
from simple_game.components.avatar import Avatar


food_store = FoodStore()


def consume_food_loop(avatar: Avatar) -> None:
    food_store.show_info()

    while avatar.check_broke():
        print("\nChoose food or type exit to leave")

        food_name = input("food name: ")

        if food_name == "exit":
            break

        for food in food_store.get_items():
            if food.get_name() == food_name:
                avatar.purchase(food)
                avatar.consume(food)
