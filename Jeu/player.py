class Joueur ():
    def __init__ (self,pseudo):
        self.pseudo = pseudo             
        self.deck = []
        self.points = 0
    def points(self, points_gagnés):
        self.points += points_gagnés