import random

# Constants
POPULATION_SIZE = 500  # Increased population size
MUTATION_RATE = 0.2     # Adjusted mutation rate
MAX_GENERATIONS = 5000  # Increased number of generations
BOARD_SIZE = 8

class Individual:
    def __init__(self):
        # Represents queen positions
        self.genes = [random.randint(0, BOARD_SIZE - 1) for _ in range(BOARD_SIZE)]
        self.fitness = 0

    def calcfitness(self):
        fitness = 0
        # Compare every pair of queens
        for i in range(BOARD_SIZE):
            for j in range(i + 1, BOARD_SIZE):
                # Check if queens are not in the same row or diagonal
                if self.genes[i] != self.genes[j] and abs(self.genes[i] - self.genes[j]) != j - i:
                    fitness += 1
        self.fitness = fitness

def initpopulation():
    return [Individual() for _ in range(POPULATION_SIZE)]

def crossover(parent1, parent2):
    crossover_point = random.randint(0, BOARD_SIZE - 1)  # Pick a random crossover point
    offspring = Individual()
    offspring.genes[:crossover_point] = parent1.genes[:crossover_point]
    offspring.genes[crossover_point:] = parent2.genes[crossover_point:]
    return offspring

def mutate(individual):
    random_position = random.randint(0, BOARD_SIZE - 1)
    individual.genes[random_position] = random.randint(0, BOARD_SIZE - 1)

def selection(population):
    tournament_size = 5  # Tournament size
    best = random.choice(population)
    
    for _ in range(1, tournament_size):
        competitor = random.choice(population)
        if competitor.fitness > best.fitness:
            best = competitor

    return best

def carrybestIndividual(population):
    best_index = max(range(len(population)), key=lambda i: population[i].fitness)
    return population[best_index]

def print_solution(individual):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if individual.genes[i] == j:
                print("Q ", end="")
            else:
                print("* ", end="")
        print()

def main():
    population = initpopulation()

    generation = 0
    while generation < MAX_GENERATIONS:
        for individual in population:
            individual.calcfitness()
            if individual.fitness == 28:  # 28 is the maximum fitness (no two queens attacking)
                print_solution(individual)
                return

        new_population = [carrybestIndividual(population)]  # Carry over the best individual (elitism)

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)
            offspring = crossover(parent1, parent2)
            if random.random() < MUTATION_RATE:
                mutate(offspring)
            new_population.append(offspring)

        population = new_population
        generation += 1

    print("No solution found within {} generations.".format(MAX_GENERATIONS))

if __name__ == "__main__":
    main()
