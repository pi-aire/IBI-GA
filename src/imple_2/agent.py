import random
import math

TABLE = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

class Agent(object):
    """
    Agent présent dans une génération
    """

    def __init__(self, mu: float, length_mdp: int,is_clone = False) -> None:
        super().__init__()
        self.mu = mu
        if not is_clone:
            self.geno_pwd = self.create_gpwd(length_mdp)

    def create_gpwd(self, lenght: int) -> str:
        tmp = []
        for _ in range(lenght):
            tmp.append(TABLE[random.randint(0,len(TABLE)-1)])
        return tmp

    def mutation(self) -> None:
        for i in range(len(self.geno_pwd)):
            if random.random() < self.mu:
                self.geno_pwd[i] = TABLE[random.randint(0,len(TABLE)-1)]
                
        
    def phenotype(self) -> str:
        """Convertie le génotype en phénotype
            génotype code de gray modifié
            
        Returns:
            str: phénotype
        """
        return "".join(self.geno_pwd)

    def clone(self):
        clone = Agent(self.mu,len(self.geno_pwd),True)
        clone.geno_pwd = self.geno_pwd
        return clone