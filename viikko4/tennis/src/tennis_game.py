SCORE_RESULT = 4

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.draw() 

        if self.player1_score >= SCORE_RESULT or self.player2_score >= SCORE_RESULT:
            return self.advantage_or_win()
 
        return self.form_result()    
    
    def draw(self):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        elif self.player1_score == 3:
            score = "Forty-All"
        else:
            score = "Deuce" 
        return score    

    def advantage_or_win(self):
        difference = self.player1_score - self. player2_score

        if difference == 1:
            score = "Advantage player1"
        elif difference == -1:
            score = "Advantage player2"
        elif difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def form_result(self):
        score = ""
        score += self.formulate(self.player1_score) 
        score += "-"
        score += self.formulate(self.player2_score)  
        return score

    def formulate(self, score):
        if score == 0:
            score = "Love"
        elif score == 1:
            score = "Fifteen"
        elif score == 2:
            score = "Thirty"
        elif score == 3:
            score = "Forty" 
        return score  
