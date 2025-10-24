import random
import matplotlib.pyplot as plt

class Region:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        
RegionA = Region("A")
RegionB = Region("B")
RegionC = Region("C")
RegionD = Region("D")
RegionE = Region("E")
RegionF = Region("F")

RegionA.neighbors = [RegionB, RegionC]
RegionB.neighbors = [RegionA, RegionC, RegionD]
RegionC.neighbors = [RegionA, RegionB, RegionD]
RegionD.neighbors = [RegionB, RegionC, RegionE]
RegionE.neighbors = [RegionD]

REGIONS = [RegionA, RegionB, RegionC, RegionD, RegionE, RegionF]


class Map:
    def __init__(self):
        self.regions = REGIONS
        
        self.map = [-1] * len(REGIONS)
        self.colors = range(4)
        
        for i in range(len(REGIONS)):
            self.map[i] = random.choice(self.colors)
        
    def fitness(self):
        conflicts = 0
        used_colors = set()
        
        for i, region in enumerate(self.regions):
            used_colors.add(self.map[i])
            for neighbor in region.neighbors:
                neighbor_index = self.regions.index(neighbor)
                if self.map[i] == self.map[neighbor_index]:
                    conflicts += 1
                    
        conflicts //= 2
        
        return -(conflicts * 100 + len(used_colors))
    
    def print_map(self):
        for i, region in enumerate(self.regions):
            print(f"Region {region.name}: Color {self.map[i]}")
            
            
def start_evolution(population_size=10, generations=100, mutation_rate=0.1):
    best_map = None
    best_fitness_over_time = []
    average_fitness_over_time = []
    population = [Map() for _ in range(population_size)]
    
    for generation in range(generations):
        population.sort(key=lambda m: m.fitness(), reverse=True)
        
        best_fitness_over_time.append(population[0].fitness())
        average_fitness = sum(m.fitness() for m in population) / population_size
        average_fitness_over_time.append(average_fitness)
        
        if best_map is None or population[0].fitness() > best_map.fitness():
            best_map = population[0]
            print(f"Generation {generation}, Best fitness: {best_map.fitness()}")
        
        next_generation = []
        
        while len(next_generation) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            crossover_point = random.randint(1, len(REGIONS) - 2)
            
            # Child 1
            child_map_colors = parent1.map[:crossover_point] + parent2.map[crossover_point:]
            child = Map()
            child.map = child_map_colors
            mutation(child, mutation_rate)
            next_generation.append(child)
            
            # Child 2
            child_map_colors = parent2.map[:crossover_point] + parent1.map[crossover_point:]
            child = Map()
            child.map = child_map_colors
            mutation(child, mutation_rate)
            next_generation.append(child)
            
        population = next_generation
        
    if best_map:
        print("Best map found:")
        best_map.print_map()
        
    plot_fitness(best_fitness_over_time, average_fitness_over_time)
    

def tournament_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda board: board.fitness())
        
def mutation(m, mutation_rate):
    for i in range(len(m.regions)):
        if random.random() < mutation_rate:
            m.map[i] = random.choice(m.colors)
        
def plot_fitness(best_fitness_over_time, average_fitness_over_time):
    generations = range(len(best_fitness_over_time))
    plt.plot(generations, best_fitness_over_time, label='Best Fitness')
    plt.plot(generations, average_fitness_over_time, label='Average Fitness')
    plt.plot(generations, [0] * len(generations), label='Max Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness over Generations')
    plt.legend()
    plt.show()
        
if __name__ == "__main__":
    start_evolution()
    
    
    