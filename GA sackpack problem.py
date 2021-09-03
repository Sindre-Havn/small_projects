"""     Genetic algorithm implementation     """


# The goal of the sackpack problem is to achieve the highest possible
# value of items in your sackpack, while holding the weight limit.

import numpy as np
from matplotlib import pyplot as plt
import math

POPULATION_SIZE = 20   # 100
GENERATIONS = 50        #  20
CROSSOVER_RATE = 0.4    #   0.4
MUTATION_RATE = 0.1     #   0.1
MUTATION_OCCURANCE = 3
ITEM_VALUE  = np.array([4,2,2,1,10,6,7,9,8,1,2,4,5,4,16,8,4,3,21,8]) # np.array([4,2,2,1,10,6,7,9,8,1])
ITEM_WEIGHT = np.array([12,2,1,1,4,4,3,4,3,2,3,6,2,4,10,11,4,1,11,9]) # np.array([12,2,1,1,4,4,3,4,3,2])
LIMIT = math.ceil(1.6*len(ITEM_WEIGHT))  # can have max 16kg in the sackpack    16


#np.random.seed(1)  # Choses the psudo-random sequence

class GA:
    def __init__(self):
        self.population = np.random.random((POPULATION_SIZE,len(ITEM_VALUE))) >= 0.5
        self.fitness = None
        self.best_fitness_in_generation = None

    def fitness_func(self):
        """Calculates the fitness for every cromosom in the population"""
        self.fitness = np.zeros((len(self.population)))
        for idx in range(len(self.population)):
            value = sum(ITEM_VALUE[self.population[idx]])
            weight = sum(ITEM_WEIGHT[self.population[idx]])
            if weight >= LIMIT:
                value = 0
            self.fitness[idx] = value
    
    def crossover(self):
        """Selects parents based on their fitness score and uses 'Multi point crossover' to produce offsprings"""
        roulett_wheel = np.array([])
        for individual in range(len(self.population)):
            for iter_val in range(int(self.fitness[individual])):
                roulett_wheel = np.append(roulett_wheel, individual)
        parents = np.array([])
        for i in range(len(self.population)):
            if np.random.random() < CROSSOVER_RATE:
                parents = np.append(parents, np.random.choice(roulett_wheel))
        offsprings = np.zeros((1,len(ITEM_VALUE)))
        for parent in range(0,len(parents)-1,2):
            parent1 = self.population[int(parents[parent])]
            parent2 = self.population[int(parents[parent+1])]
            cut1 = int(np.random.randint(0,len(ITEM_WEIGHT)-2))
            cut2 = int(np.random.randint(cut1,len(ITEM_WEIGHT)-1) +1)
            genes1 = parent1[cut1:cut2]
            genes2 = parent2[cut1:cut2]
            parent1 = np.delete(parent1, np.s_[cut1:cut2], axis=0)
            parent2 = np.delete(parent2, np.s_[cut1:cut2], axis=0)
            child1 = np.insert(parent1,cut1,genes2)
            child2 = np.insert(parent2,cut1,genes1)
            offsprings = np.append(offsprings, np.array([child1]), axis=0)
            offsprings = np.append(offsprings, np.array([child2]), axis=0)
        offsprings  = np.delete(offsprings, 0, axis=0)
        self.population = np.append(self.population, offsprings, axis=0).astype(bool)


    def mutation(self):
        """Mutates up to 3 alleles in a random individuals genes. The best individual in the population can NOT be mutated"""
        elite_chromosom = self.population[np.where(self.fitness==max(self.fitness))[0][0]]
        self.population = np.delete(self.population, elite_chromosom, axis=0)
        for i in range(len(self.population)):
            if np.random.random() <= MUTATION_RATE:
                print("\nMutation occured!")
                unlucky_one = self.population[np.random.randint(0,len(self.population)-1),:]
                print("Before:", unlucky_one)
                unlucky_idx = np.where(self.population==unlucky_one)[0][0]
                for i in range(np.random.randint(1,MUTATION_OCCURANCE)):
                    idx = np.random.randint(0,len(ITEM_WEIGHT)-1)
                    unlucky_one[idx] = 1 if unlucky_one[idx] == 0 else 0
                print("After:", unlucky_one, "\n")
                self.population[unlucky_idx] = unlucky_one
            self.population = np.append(self.population, np.array([elite_chromosom]), axis=0)

    def selection(self):
        """Selects which indivduals are being included in the next generation"""
        self.fitness_func()
        new_generation = np.zeros((1,len(ITEM_VALUE)))
        self.best_fitness_in_generation = max(self.fitness)
        for idx in range(POPULATION_SIZE):
            survivor = self.population[np.argmax(self.fitness)]
            self.fitness = np.delete(self.fitness, np.argmax(self.fitness))
            new_generation = np.append(new_generation, np.array([survivor]), axis=0)
        new_generation = np.delete(new_generation, 0, axis=0)
        self.population = new_generation.astype(bool)

        
ga = GA()

best_fitnesses = np.array([])
plt.xlabel("Generations")
plt.ylabel("Fitness")

for i in range(GENERATIONS):
    print("Generation:", i)
    ga.fitness_func()
    ga.crossover()
    ga.mutation()
    ga.selection()
    best_fitnesses = np.append(best_fitnesses, ga.best_fitness_in_generation)
    plt.plot(best_fitnesses)
    
print(ga.population)
print(best_fitnesses)
plt.show()
