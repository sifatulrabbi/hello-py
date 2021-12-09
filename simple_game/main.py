from simple_game.components.avatar import Avatar
from simple_game.components.store import Store
from simple_game.components.gig_store import GigStore
from simple_game.components.food import Food


def main() -> None:
    store = Store(
        {
            "pizza": Food("Pizza", 40, 15.6, "human"),
            "cola": Food("Cola", 3, 1.25, "all"),
            "burger": Food("Burger", 25, 8.5, "human"),
            "mars_soil": Food("Mars Soil", 150, 30.25, "alien"),
        }
    )
    foods = store.get_items()
    gigs = GigStore().get_items()

    new_av = Avatar("Peter", "human")
    new_av.show_status()

    new_av.consume(foods["pizza"])
    new_av.income(gigs["build_server"])

    new_av.show_status()
