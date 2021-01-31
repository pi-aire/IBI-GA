import imple_2.agent as a
import numpy as np
import math
import random
import matplotlib.pyplot as plt 


class Genetic_algorithm(object):
    """
    Réalise l'exécution de l'algorithme génétique
    """

    def __init__(self,
                 nb_agent: int, nbgen: int, pc: float, mu: float,c:float, nb_call: int,
                 evaluation_function,
                 student_id: int, length_mdp: int) -> None:
        super().__init__()
        self.gen: int = 0
        self.nb_gen: int = nbgen
        self.pc: float = pc
        self.mu: float = mu
        self.c: float = c
        self.length_mdp: int = length_mdp
        self.student_id = student_id
        self.fit_func = evaluation_function
        self.agents: list = []
        self.nb_call = nb_call
        self.create_agent(nb_agent)
        self.total_call = 0  # nombre de call réalisé par les agents


    def create_agent(self, nb_agent: int) -> None:
        for _ in range(nb_agent):
            self.agents.append(
                a.Agent(self.mu, self.length_mdp))

    def fitness(self,phenotypes) -> float:
            sum = [0.0 for _ in range(len(self.agents))]
            self.total_call += self.nb_call
            for c in range(self.nb_call):
                result = self.fit_func(self.student_id,phenotypes)
                for i in range(len(self.agents)):
                   sum[i] += result[i]
                   if c == (self.nb_call-1):
                       sum[i] /= self.nb_call
            return sum
            
    def evaluation(self) -> dict:
        fitness = dict()
        isfind = False           
        list = self.fitness([agent.phenotype() for agent in self.agents])
        # On convertie en dictionnaire
        for i in range(len(list)):
            fitness[i]= list[i] 
            isfind = isfind or (list[i] == 1)      
        # On réalise le classement
        fitness = {key: value for key, value in sorted(
            fitness.items(), key=lambda item: -item[1])}
        return fitness, isfind

    def ranking_lineaire(self, fitness: dict):
        size = len(fitness)
        rank = [0 for i in range(size)]
        r = size
        for i in fitness:
            rank[i] = (2/(size*(size-1)))*(r-1)
            r -= 1
            
        return rank
    
    def ranking_expo(self, fitness: dict):
        size = len(fitness)
        rank = [0 for i in range(size)]
        r = size
        for i in fitness:
            rank[i] = (self.c - 1) / (math.pow(self.c, size)-1)
            rank[i] *= math.pow(self.c,size-r) 
            r -= 1
        # plt.plot([i for i in range(size)],rank)
        # plt.show()
        return rank

    def wheel(self, proba):
        """[summary]

        Args:
            ranking ([type]): Les proba pour chaque agent

        Returns:
            int: indice de l'agent choisi aléatoirement
        """
        index = np.random.choice(np.arange(0, len(proba)), p=proba)
        return index

    def cross_over(self, a1: a.Agent, a2: a.Agent):
        """Fait des coupure avec des valeurs de taille d'une lettre
        Args:
            a1 ([type]): agent 1
            a2 ([type]): agent 2
        """
        cutpos = random.randint(1, self.length_mdp - 1)
        tmp = a1.geno_pwd[:cutpos]
        a1.geno_pwd[:cutpos] = a2.geno_pwd[:cutpos]
        a2.geno_pwd[:cutpos] = tmp

    def new_generation(self):
        # Selection
        self.fitness_v, isfind = self.evaluation()  # fitness trillé
        proba = self.ranking_expo(self.fitness_v)  # classement des agents
        
        index = [*self.fitness_v.keys()][0]
        pwd = self.agents[index].phenotype()
        print(f"generation: {self.gen}, mdp: {pwd} : {len(pwd)} , score {self.fitness_v[index]}")
        
        # On s'arrête si on trouve le mot de passe
        if isfind:
            return True, self.fitness_v[index]
        
        # Création de la nouvelle génération
        new_gen = []
        while len(new_gen) < len(self.agents):
            child1 = self.agents[self.wheel(proba)].clone()
            child2 = self.agents[self.wheel(proba)].clone()
            if random.random() < self.pc:
                self.cross_over(child1, child2)
            child1.mutation()
            child2.mutation()
            new_gen.extend([child1, child2])
        self.agents = new_gen
        return False, self.fitness_v[index]

    def resolution(self) -> str:
        end = False
        scores = []
        while not end and self.gen <= self.nb_gen:
            end, score = self.new_generation()
            scores.append(score)
            self.gen += 1
        f = plt.figure() 
        f.set_figwidth(10) 
        f.set_figheight(6)
        plt.plot([i for i in range(self.gen)],scores)
        plt.xlabel("Génération")
        plt.ylabel("Fitness")
        plt.title("Evolution de la fitness max en fonction de la génération")
        plt.suptitle(f"Nb agent: {len(self.agents)}, Nb gen: {self.gen}, Proba c-o: {self.pc}\n Taux de mutation: {self.mu}, C: {self.c}")
        last = scores.pop()
        plt.savefig(f"../img/impl2_{self.gen}_{last}.png")
