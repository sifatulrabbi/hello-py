class Food:
    name: str
    for_occult: str
    calories: int

    def __init__(self, name: str, for_occult: str, calories: str = 10) -> None:
        self.name = name
        self.for_occult = for_occult
        self.calories = calories
