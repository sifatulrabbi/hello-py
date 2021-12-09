from food import Food


class Person:
    name: str
    age: int
    loves: list[str]
    occult: str
    consumed_calories: int = 2000

    def __init__(self, name: str, age: int, loves: list[str], occult: str) -> None:
        self.name = name
        self.age = age
        self.loves = loves
        self.occult = occult

    def get_hello(self) -> None:
        print(f"Hi I'm {self.name}. How are you?")

    def get_name(self) -> str:
        return self.name

    def give_food(self, food: Food) -> None:
        if food.for_occult == self.occult:
            self.increase_calorie(food.calories)

            print(
                f"{self.name}:\n"
                f"{food.name} was yummy!\n"
                f"And I've gained {food.calories} cals.\n"
                f"now my calorie count is {self.consumed_calories} cals\n"
            )
        else:
            print(
                f"{self.name}:\n"
                f"I cannon eat {food.name} because I'm {self.occult}\n"
            )

    def increase_calorie(self, amount: int) -> None:
        self.consumed_calories += amount

    def decrease_calorie(self, amount: int) -> None:
        self.consumed_calories -= amount
