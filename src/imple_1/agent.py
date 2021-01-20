import random
import math

TABLE = ["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

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
        return [random.randint(0,1) for _ in range(lenght*6)]

    def mutation(self) -> None:
        for bit in self.geno_pwd:
            if random.random() < self.mu:
                bit = (bit+1)%2
                break
        
    def phenotype(self) -> str:
        """Convertie le génotype en phénotype
            génotype code de gray modifié
            
        Returns:
            str: phénotype
        """
        result = ""
        for i in range(int(len(self.geno_pwd)/6)):
            posi = i*6
            total = 0
            for j in range(6):
                total += math.pow(2,5-j) * self.geno_pwd[posi+j]
            if total < len(TABLE):
                result += TABLE[int(total)]
        return result

    def clone(self):
        clone = Agent(self.mu,len(self.geno_pwd),True)
        clone.geno_pwd = self.geno_pwd.copy()
        return clone