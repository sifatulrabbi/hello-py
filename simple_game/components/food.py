class Food:
    __name: str
    __stamina: int
    __price: float
    __for_occult: str

    def __init__(self, name: str, stamina: int, price: float, for_occult: str) -> None:
        self.__name = name
        self.__price = price
        self.__for_occult = for_occult
        self.__stamina = stamina

    def get_stamina(self) -> int:
        return self.__stamina

    def get_for_occult(self) -> str:
        return self.__for_occult

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def show_log(self) -> None:
        print(f"name: {self.__name}, price: {self.__price}")
