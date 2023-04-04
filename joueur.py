class Joueur:
    def __init__(self, identifiant, mdp, age) :
        self.id =  identifiant
        self.mdp = mdp
        self.age = age 
        self.win = 0
        self.lose = 0
        self.main = [] # ajouté pour distribuer les cartes 
        