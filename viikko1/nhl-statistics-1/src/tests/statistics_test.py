import unittest
from statistics import Statistics
from player import Player

import sys
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG
strea_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(strea_handler)

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_sorts_by_points(self):
        top_players_from_stub = [self.statistics._players[1], self.statistics._players[4]]
        top_players_from_method = self.statistics.top_scorers(1)
        self.assertCountEqual(top_players_from_stub, top_players_from_method)
    
    def test_search_returns_correct_player(self):
        returned_player = self.statistics.search("Semenko")
        self.assertEqual(returned_player.name, "Semenko")
        self.assertEqual(returned_player.team, "EDM")

    def test_search_returns_None_if_player_doesnt_exists(self):
        returned_player = self.statistics.search("Unkwnow")
        self.assertEqual(returned_player, None)

    def test_team_contains_correct_players(self):
        players_from_stub = [self.statistics._players[0], self.statistics._players[2], self.statistics._players[4]]
        players_from_method = self.statistics.team("EDM")
        self.assertCountEqual(players_from_stub, players_from_method)