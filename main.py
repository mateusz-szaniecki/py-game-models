import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for player_data in players.values():
            guild_data = player_data["guild"]

            if guild_data:
                Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"],
                )


if __name__ == "__main__":
    main()
