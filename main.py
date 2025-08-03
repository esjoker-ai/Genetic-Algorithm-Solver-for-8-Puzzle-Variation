import random

class Board:
    def __init__(self, g=None):
        self.size = 9
        self.genes = g
        self.fitness = 0
        if self.genes:
            self.set_fitness()

    def init_board(self):
        self.genes = random.sample(range(0, 9), self.size)
        self.set_fitness()

    def set_fitness(self):
        self.fitness = 0  # Reset fitness before re-evaluating
        for i in range(self.size - 1):
            if self.genes[i] == (i + 1):
                self.fitness += 1
        if self.genes[8] == 0:
            self.fitness += 1


class GeneticAlgorithm:
    def __init__(self):
        self.population = []

    def init_population(self, p_size):
        for _ in range(p_size):
            gene = Board()
            gene.init_board()
            self.population.append(gene)

    def sort_genes(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)

    def crossover_population(self):
        new_population = []
        for i in range(0, int(len(self.population) / 2), 2):
            parent1 = self.population[i]
            parent2 = self.population[i + 1]

            new_population.append(self.crossover(parent1, parent2, 3))
            new_population.append(self.crossover(parent2, parent1, 3))
            new_population.append(self.crossover(parent1, parent2, 6))
            new_population.append(self.crossover(parent2, parent1, 6))

        for i in range(len(new_population)):
            if random.randint(0, 100) < 50:
                new_population[i] = self.mutation(new_population[i])

        self.population = new_population

    @staticmethod
    def mutation(b):
        ind = random.randint(0, 8)
        b.genes[ind] = random.randint(0, 8)
        b.set_fitness()
        return b

    @staticmethod
    def crossover(p1, p2, cutoff):
        new_genes = p1.genes[:cutoff] + p2.genes[cutoff:]
        child = Board(new_genes)
        return child

    def print_board(self):
        for b in self.population:
            print(b.genes[0:3])
            print(b.genes[3:6])
            print(b.genes[6:9])
            print("Fitness:", b.fitness)
            print("-----")


if __name__ == "__main__":
    ga = GeneticAlgorithm()
    ga.init_population(8)
    ga.sort_genes()

    print("Initialized Population")
    ga.print_board()

    while ga.population[0].fitness < 9:
        ga.crossover_population()
        ga.sort_genes()
        print("New Generation")
        ga.print_board()

    print("🎉 Solved Board is:", ga.population[0].genes)
