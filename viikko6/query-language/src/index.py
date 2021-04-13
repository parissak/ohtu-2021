from pprint import pprint
from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m1 = query.playsIn("PHI").hasAtLeast(5,"assists").hasFewerThan(5, "goals").build()
    m2 = query.playsIn("EDM").hasAtLeast(40,"points").build()
    m3 = query.playsIn("VGK").build()

    matcher = query.oneOf(m1, m2, m3).build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()