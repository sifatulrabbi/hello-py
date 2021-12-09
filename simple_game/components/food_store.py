from simple_game.components.food import Food


class FoodStore:
    name: str = "Food store"
    __items: list[Food]

    def __init__(self) -> None:
        self.__items = [
            Food("Pizza", 40, 15.6, "human"),
            Food("Cola", 3, 1.25, "all"),
            Food("Burger", 25, 8.5, "human"),
            Food("Mars Soil", 150, 30.25, "alien"),
        ]

    def get_items(self) -> list[Food]:
        return self.__items

    def show_info(self) -> None:
        print(f"\n*** {self.name} ***")

        for item in self.__items:
            print(
                f"food: {item.get_name()}; price: {item.get_price()}$; / stamina gain: {item.get_stamina()};"
            )
