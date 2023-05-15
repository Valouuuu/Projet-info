class Joueur ():
    def __init__ (self,pseudo,joueur):
        self.numero_joueur = joueur
        self.pseudo = pseudo             
        self.deck = []
        self.points = 0
        self.à_mon_tour = False
    
    
    def points(self, points_gagnés):
        self.points += points_gagnés