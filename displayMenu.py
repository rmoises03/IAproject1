import utils
import hill_climbing
import simulated_annealing
import tabu_search
import genetic_algorithm
import greedy
import classes
import antcolony

def main():
    files = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
    initial_solutions = ["random_solution", "random_solution_per_signup", "greedy_solution"]
    while True:
        print("Menu:")
        print("1. Hill Climbing")
        print("2. Hill Climbing First Accept")
        print("3. Simulated Annealing")
        print("4. Tabu Search")
        print("5. Genetic Algorithm")
        print("6. Ant Colony Optimization")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4','5','6']:
            print("Choose a file:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            file_choice = input("Enter your choice: ")
            if not file_choice.isdigit() or int(file_choice) < 1 or int(file_choice) > len(files):
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue
            file_name = files[int(file_choice) - 1]
            if choice in ['1', '2', '3', '4','5']:
                print("Choose an initial solution:")
                for i, solution in enumerate(initial_solutions, start=1):
                    print(f"{i}. {solution}")
                solution_choice = input("Enter your choice: ")
                if not solution_choice.isdigit() or int(solution_choice) < 1 or int(solution_choice) > len(initial_solutions):
                    print("Invalid choice. Please enter a number between 1 and 3.")
                    continue
                initial_solution = initial_solutions[int(solution_choice) - 1]

                if choice == '1':
                    # Run Hill Climbing
                    libraries, book_scores, days = utils.readFile(file_name)
                    if initial_solution == 'random_solution':
                        initial_solution_random = utils.random_solution(libraries, book_scores, days)
                    elif initial_solution == 'random_solution_per_signup':
                        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
                    elif initial_solution == 'greedy_solution':
                        empty_solution = classes.State([], {}, book_scores, [], 0)
                        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)

                    best_solution_from_hill_climbing = hill_climbing.hill_climbing(initial_solution_random, days, libraries)
                    total_score = utils.get_values_from_dict(best_solution_from_hill_climbing.books_explored, book_scores)
                    print("Hill Climbing: ", total_score)
                elif choice == '2':
                    # Run Hill Climbing
                    libraries, book_scores, days = utils.readFile(file_name)
                    if initial_solution == 'random_solution':
                        initial_solution_random = utils.random_solution(libraries, book_scores, days)
                    elif initial_solution == 'random_solution_per_signup':
                        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
                    elif initial_solution == 'greedy_solution':
                        empty_solution = classes.State([], {}, book_scores, [], 0)
                        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)

                    best_solution_from_hill_climbing = hill_climbing.hill_climbing_first_accept(initial_solution_random, days, libraries)
                    total_score = utils.get_values_from_dict(best_solution_from_hill_climbing.books_explored, book_scores)
                    print("Hill Climbing First Accept: ", total_score)
                elif choice == '3':
                # Run Simulated Annealing
                    libraries, book_scores, days = utils.readFile(file_name)
                    if initial_solution == 'random_solution':
                        initial_solution_random = utils.random_solution(libraries, book_scores, days)
                    elif initial_solution == 'random_solution_per_signup':
                        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
                    elif initial_solution == 'greedy_solution':
                        empty_solution = classes.State([], {}, book_scores, [], 0)
                        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)

                    cooling_rate = float(input("Enter the cooling rate (between 0 and 1): "))
                    max_iterations = int(input("Enter the maximum number of iterations: "))
                    stop_temperature = float(input("Enter the stopping temperature: "))
                    best_solution_from_simulated_annealing = simulated_annealing.simulated_annealing(initial_solution_random, days, libraries, cooling_rate, max_iterations, stop_temperature)
                    total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored, book_scores)
                    print("Simulated Annealing: ", total_score)
                elif choice == '4':
                    # Run Tabu Search
                    libraries, book_scores, days = utils.readFile(file_name)
                    if initial_solution == 'random_solution':
                        initial_solution_random = utils.random_solution(libraries, book_scores, days)
                    elif initial_solution == 'random_solution_per_signup':
                        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
                    elif initial_solution == 'greedy_solution':
                        empty_solution = classes.State([], {}, book_scores, [], 0)
                        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)
                    tabu_size = int(input("Enter the tabu size: "))
                    max_iterations = int(input("Enter the maximum number of iterations: "))

                    best_solution_from_tabu_search = tabu_search.tabu_search(initial_solution_random, tabu_size, max_iterations, libraries)
                    total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored, book_scores)
                    print("Tabu Search: ", total_score)

                elif choice == '5':
                    # Run Genetic Algorithm
                    libraries, book_scores, days = utils.readFile(file_name)
                    if initial_solution == 'random_solution':
                        initial_solution_random = utils.random_solution(libraries, book_scores, days)
                    elif initial_solution == 'random_solution_per_signup':
                        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
                    elif initial_solution == 'greedy_solution':
                        empty_solution = classes.State([], {}, book_scores, [], 0)
                        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)
                    number_generations = int(input("Enter the number of generations: "))
                    population_size = int(input("Enter the population size: "))
                    mutation_rate = float(input("Enter the mutation rate (between 0 and 1): "))
                    tournament_size = 0
                    selected = int(input("Enter 0 for roulette selection or 1 for tournament selection: "))
                    if selected == 1:
                        tournament_size = int(input("Enter the tournament size: "))
                    population = [utils.random_solution(libraries, book_scores, days) for _ in range(population_size)]
                    best_solution_from_genetic_algorithm = genetic_algorithm.genetic_algorithm(population, days, number_generations, tournament_size, mutation_rate,libraries,selected)
                    total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored, book_scores)
                    print("Genetic Algorithm: ", total_score)
            elif choice == '6':
                if choice == '6':
                    # Run the Ant Colony Algorithm
                    libraries, book_scores, days = utils.readFile(file_name)
                    num_iterations = int(input("Enter the number of iterations: "))
                    num_ants = int(input("Enter the number of ants: "))
                    evaporation_rate = float(input("Enter the evaporation rate: "))
                    initial_pheromone = float(input("Enter the initial pheromone: "))
                    alpha = float(input("Enter the alpha value: "))
                    beta = float(input("Enter the beta value: "))
                    best_solution_from_ant_colony = antcolony.ant_colony_optimization(libraries, book_scores, days, num_iterations, num_ants, evaporation_rate, initial_pheromone, alpha, beta)
                    total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored, book_scores)
                    print("Ant Colony Optimization: ", total_score)
        elif choice == '7':
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()