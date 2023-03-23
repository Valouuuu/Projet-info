class Joueur:
    def __init__(identifiant, mdp, age) :
        self.id =  identifiant
        self.mdp = mdp
        #self.age = age (7 ans min si on a le temps)
        self.win = 0
        self.lose = 0