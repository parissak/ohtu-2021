from pprint import pprint
from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, Not, Or, PlaysIn
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query
            .playsIn("NYR")
            .hasAtLeast(5,"goals")
            .HasFewerThan(10, "goals")
            .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()