class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

        self.numbers = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.draw() 

        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_or_win()
 
        return self.not_decisive()    
    
    def draw(self):
        if self.player1_score < 4:
            return f"{self.numbers[self.player1_score]}-All"
        else:
            return "Deuce"   

    def advantage_or_win(self):
        difference = self.player1_score - self. player2_score
        player = "player1" if difference > 0 else "player2" 

        if abs(difference) == 1:
            return f"Advantage {player}"

        return f"Win for {player}"
    
    def not_decisive(self):
        return self.numbers[self.player1_score] + "-" + self.numbers[self.player2_score]