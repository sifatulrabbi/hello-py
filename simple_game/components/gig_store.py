from simple_game.components.store import Store
from simple_game.components.gig import Gig


class GigStore(Store):
    def __init__(self) -> None:
        super().__init__(
            {
                "do_maths": Gig("Do maths", 1.25, 1),
                "build_webpage": Gig("Build Webpage", 5, 3),
                "build_server": Gig("Build Server", 1000, 85),
            }
        )
