from simple_game.components.food import Food


class Store:
    name: str
    __items: dict

    def __init__(self, items: dict) -> None:
        self.name = "Generic Store"
        self.__items = items

    def get_items(self) -> dict[str:Food]:
        return self.__items
