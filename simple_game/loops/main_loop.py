from simple_game.components.avatar import Avatar
from simple_game.loops.consume_food_loop import consume_food_loop
from simple_game.loops.do_gig_loop import do_gig_loop


def main_loop(avatar: Avatar) -> None:
    while not avatar.check_death():
        user_input = input("\nconsume or do_gig ? ")

        if user_input == "consume":
            consume_food_loop(avatar)

        elif user_input == "do_gig":
            do_gig_loop(avatar)

        elif user_input == "exit":
            print("\nQuiting the game...")
            break
