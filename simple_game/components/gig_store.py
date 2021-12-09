from simple_game.components.gig import Gig


class GigStore:
    name: str = "Gig store"
    __items: list[Gig]

    def __init__(self) -> None:
        self.__items = [
            Gig("Do maths", 1.25, 1),
            Gig("Build Webpage", 5, 3),
            Gig("Build Server", 1000, 85),
        ]

    def get_items(self) -> list[Gig]:
        return self.__items

    def show_info(self) -> None:
        print(f"\n*** {self.name} ***")

        for item in self.__items:
            print(
                f"gig: {item.get_name()}; earn: {item.get_paycheck()}$; / stamina loss: {item.get_stamina_loss()};"
            )
