from simple_game.components.gig_store import GigStore
from simple_game.components.avatar import Avatar


gig_store = GigStore()


def do_gig_loop(avatar: Avatar) -> None:
    gig_store.show_info()

    while avatar.check_broke():
        print("\nChoose Gig or type exit to leave")

        gig_name = input("Gig name: ")

        if gig_name == "exit":
            break

        for gig in gig_store.get_items():
            if gig.get_name() == gig_name:
                avatar.do_gig(gig)
