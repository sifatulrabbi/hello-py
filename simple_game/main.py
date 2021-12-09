from simple_game.components.avatar import Avatar
from simple_game.loops.main_loop import main_loop


def main() -> None:
    avatar: Avatar

    print("🕹️ Welcome to my simple terminal game 🕹️")

    while True:
        av_name: str = input("Type your avatar name: ")
        av_occult: str = input("Choose your occult:\n- human \n- alien\n ?: ")

        if av_name and av_occult == "human" or av_occult == "alien":
            break

    avatar = Avatar(av_name, av_occult)

    print(f"\n✨ Avatar created ✨")
    avatar.show_status()

    main_loop(avatar)
