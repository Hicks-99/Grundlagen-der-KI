import random
import matplotlib.pyplot as plt

class Board:
    def __init__(self, size = 8, *args, **kwargs):
        self.size = size
        self.queens = [-1] * size
        
        for i in range(size):
            self.queens[i] = random.randint(0, size - 1)
        
    def print_board(self):
        for col in self.queens:
            row_str = ""
            for c in range(self.size):
                if c == col:
                    row_str += " Q "
                else:
                    row_str += " . "
            print(row_str)
    
    def fitness(self):
        conflicts = 0
        for r1 in range(self.size):
            for r2 in range(r1 + 1, self.size):
                c1 = self.queens[r1]
                c2 = self.queens[r2]
                if c1 == c2 or abs(c1 - c2) == abs(r1 - r2):
                    conflicts += 1
        return -conflicts


def start_evolution(population_size=15, generations=100, mutation_rate=0.1):
    best_board = None
    best_fitness_over_time = []
    average_fitness_over_time = []
    population = [Board() for _ in range(population_size)]
    
    for generation in range(generations):
        population.sort(key=lambda board: board.fitness(), reverse=True)
        
        best_fitness_over_time.append(population[0].fitness())
        average_fitness = sum(board.fitness() for board in population) / population_size
        average_fitness_over_time.append(average_fitness)
        
        if population[0].fitness() == 0:
            print(f"Solution found in generation {generation}:")
            population[0].print_board()
            plot_fitness(best_fitness_over_time, average_fitness_over_time)
            return
        
        if best_board is None or population[0].fitness() > best_board.fitness():
            best_board = population[0]
            print(f"Generation {generation}, Best fitness: {best_board.fitness()}")
        
        next_generation = []
        
        while len(next_generation) < population_size:
            # Use tournament selection instead of random choice
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            crossover_point = random.randint(1, parent1.size - 2)
            
            # Child 1
            child_queens = parent1.queens[:crossover_point] + parent2.queens[crossover_point:]
            child = Board()
            child.queens = child_queens
            mutation(child, mutation_rate)
            next_generation.append(child)
            
            # Child 2
            child_queens = parent2.queens[:crossover_point] + parent1.queens[crossover_point:]
            child = Board()
            child.queens = child_queens
            mutation(child, mutation_rate)
            next_generation.append(child)
            
        population = next_generation
        
    print("No solution found.")
    if best_board:
        print("Best board found:")
        best_board.print_board()
        
    plot_fitness(best_fitness_over_time, average_fitness_over_time)
    

def tournament_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda board: board.fitness())
        
def mutation(board, mutation_rate):
    for i in range(board.size):
        if random.random() < mutation_rate:
            board.queens[i] = random.randint(0, board.size - 1)
            
            
def plot_fitness(best_fitness, average_fitness):
    generations = range(len(best_fitness))
    plt.plot(generations, best_fitness, label='Best Fitness')
    plt.plot(generations, average_fitness, label='Average Fitness')
    plt.plot(generations, [0]*len(generations), label="Max Fitness")
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness over Generations')
    plt.legend()
    plt.show()
            

if __name__ == "__main__":
    start_evolution()
