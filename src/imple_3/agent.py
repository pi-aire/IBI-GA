import random
import math

TABLE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Agent(object):
    """
    Agent présent dans une génération
    """

    def __init__(self, mu: float, length_mdp: int, is_clone=False) -> None:
        super().__init__()
        self.mu = mu
        if not is_clone:
            self.geno_pwd = self.create_gpwd(length_mdp)
        self.mutations = [
            self.mutation_down,
            self.mutation_random,
            # self.mutation_random,
            self.mutation_random,
            self.mutation_switch,
            self.mutation_up,
            self.mutation_insert,
            self.mutation_shift_r,
            self.mutation_shift_l
        ]

    def create_gpwd(self, lenght: int) -> str:
        """Innitialisation aléatoire de l'individu"""
        tmp = []
        lenght_r = random.randint(12, lenght)
        for _ in range(lenght_r):
            tmp.append(TABLE[random.randint(0, len(TABLE)-1)])
        return tmp

    def mutation(self) -> None:
        """
        Fonction de mutation qui appelle aléatoirement 
        une des fonctions de mutation spécifique
        """
        if random.random() < self.mu:
            fun = random.randint(0, len(self.mutations) - 1)
            self.mutations[fun]()

    def mutation_random(self) -> None:
        """On change la valeur d'un caractère aléatoirement"""
        posi = random.randint(0, len(self.geno_pwd) - 1)
        self.geno_pwd[posi] = TABLE[random.randint(0, len(TABLE)-1)]
    
    def mutation_switch(self) -> None:
        """"""
        posi = random.randint(0, len(self.geno_pwd) - 1)
        posi_2 = random.randint(0, len(self.geno_pwd) - 1)
        tmp= self.geno_pwd[posi] 
        self.geno_pwd[posi] = self.geno_pwd[posi_2] 
        self.geno_pwd[posi_2] = tmp

    def mutation_down(self) -> None:
        """
        On enlève aléatoirement un caractère dans le génotype 
        si le nombre de caractère est supérieur à 12 caractères
        """
        if len(self.geno_pwd) > 12:
            del self.geno_pwd[random.randint(0, len(self.geno_pwd) - 1)]

    def mutation_up(self) -> None:
        """On ajoute un caractère aléatoire à une position aléatoire."""
        if len(self.geno_pwd) < 18:
            self.geno_pwd.insert(random.randint(0,len(self.geno_pwd)-1),TABLE[random.randint(0, len(TABLE)-1)])

    def mutation_shift_r(self) -> None:
        """
        On supprime le génome situé à la fin du génotype 
        et on rajoute un caractère aléatoire en première position.
        """
        self.geno_pwd.pop()
        self.geno_pwd.insert(0,TABLE[random.randint(0, len(TABLE)-1)]) 
    
    def mutation_shift_l(self) -> None:
        """
        On supprime le génome situé au début du génotype 
        et on rajoute un caractère aléatoire en dernière position
        """
        self.geno_pwd.append(TABLE[random.randint(0, len(TABLE)-1)])
        del self.geno_pwd[0] 
    
    def mutation_insert(self) -> None:
        """Intervertie de place deux caractères aléatoirement présent dans le génotype."""
        del self.geno_pwd[random.randint(0,len(self.geno_pwd)-1)]
        self.geno_pwd.insert(random.randint(0,len(self.geno_pwd)-1),TABLE[random.randint(0, len(TABLE)-1)])

    def phenotype(self) -> str:
        """Convertie le génotype en phénotype
            génotype code de gray modifié

        Returns:
            str: phénotype
        """
        return "".join(self.geno_pwd)

    def clone(self):
        """Réalise un copie profonde de l'indiviu"""
        clone = Agent(self.mu, len(self.geno_pwd), True)
        clone.geno_pwd = self.geno_pwd.copy()
        return clone
