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

            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={"description": player_data["race"]["description"]}
            )

            for skill_data in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={
                        "bonus": skill_data["bonus"],
                    }
                )

        for player_name, player_data in players.items():
            race = Race.objects.get(name=player_data["race"]["name"])

            guild = None
            if player_data["guild"]:
                guild = Guild.objects.get(name=player_data["guild"]["name"])

            Player.objects.get_or_create(
                email=player_data["email"],
                defaults={
                    "nickname": player_name,
                    "race": race,
                    "guild": guild,
                    "bio": player_data["bio"],
                }
            )


if __name__ == "__main__":
    main()
