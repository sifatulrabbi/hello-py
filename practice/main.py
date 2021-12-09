from practice.food import Food
from practice.person import Person


def main() -> None:
    me = Person("Sifatul", 20, "Programming", "human")
    alien = Person("Temujin", 2300, "Nothing", "alien")

    foods: dict[str:Food] = {
        "Chicken Burger": Food("Chicken burger", "human", 230),
        "Pizza": Food("Pizza", "human", 330),
        "Boiled Mars soil": Food("Boiled Mars soil", "alien", 5000),
    }

    me.give_food(foods["Chicken Burger"])

    alien.give_food(foods["Pizza"])

    me.give_food(foods["Boiled Mars soil"])


main()
