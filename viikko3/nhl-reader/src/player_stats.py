from player import Player
from player_reader import PlayerReader

class PlayerStats:
        def __init__(self, reader):
            self.reader = reader
            self.players = reader.get_players()
        
        def top_scorers_by_nationality(self, nationality):
            filtered_list = filter(lambda player: player.nationality == nationality, self.players)

            sorted_list = sorted(filtered_list, key=lambda x: x.goals + x.assists, reverse=True)

            return sorted_list