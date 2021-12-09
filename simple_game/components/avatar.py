from simple_game.components.food import Food
from simple_game.components.gig import Gig


class Avatar:
    __name: str
    __occult: str
    __ballance: float
    __stamina: int
    __is_dead: bool
    __is_broke: bool

    def __init__(self, name: str, occult: str) -> None:
        self.__name = name
        self.__occult = occult
        self.__ballance = 200
        self.__stamina = 70
        self.__is_dead = False
        self.__is_broke = True

    def __show_name(self) -> None:
        print(f"\n{self.__name}:")

    def show_status(self) -> None:
        self.__show_name()
        print(
            f"stamina: {self.__stamina}\n"
            f"ballance: {self.__ballance}\n"
            f"occult: {self.__occult}"
        )

    def check_death(self) -> bool:
        if self.__stamina == 0:
            self.__is_dead = True

        return self.__is_dead

    def check_broke(self) -> bool:
        if self.__ballance == 0:
            self.__is_broke = True

        return self.__is_broke

    def __increase_stamina(self, amount: int) -> None:
        if (self.__stamina + amount) > 100:
            self.__stamina = 100

        else:
            self.__stamina += amount

    def __decrease_stamina(self, gig: Gig) -> None:
        if (self.__stamina - gig.get_stamina_loss()) < 0:
            self.__stamina = 0

        else:
            self.__stamina -= gig.get_stamina_loss()

    def do_gig(self, gig: Gig) -> None:
        if self.__stamina < gig.get_stamina_loss():
            self.__show_name()
            print(f"I don't have enough stamin to do {gig.get_name()}\n")
            return

        self.__decrease_stamina(gig)
        self.__ballance += gig.get_paycheck()

        self.__show_name()
        print(f"Got {gig.get_paycheck()} dollars from gig: {gig.get_name()}\n")
        self.show_status()

    def purchase(self, food: Food) -> None:
        if (self.__ballance - food.get_price()) < 0:
            self.__ballance = 0

        else:
            self.__ballance -= food.get_price()

    def consume(self, food: Food) -> None:
        if food.get_for_occult() == self.__occult:
            self.__increase_stamina(food.get_stamina())

            self.__show_name()
            print(f"Yummy! {food.get_name()} was tasty.\n")
            self.show_status()

        elif food.get_for_occult() == "all":
            self.__increase_stamina(food.get_stamina())

        else:
            self.__show_name()
            print(f"I can't take {food.get_name()} because I'm a {self.__occult}\n")
