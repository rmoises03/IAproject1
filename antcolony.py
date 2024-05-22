import random
import utils
import classes


def ant_colony_optimization(libraries, book_scores, days, num_iterations, num_ants, evaporation_rate, initial_pheromone, alpha, beta):
    pheromones = initialize_pheromones(libraries, initial_pheromone)

    best_solution = None
    best_score = 0

    for iteration in range(num_iterations):
        solutions = []
        for _ in range(num_ants):
            solution = construct_solution(libraries, book_scores, days, pheromones, alpha, beta)
            print(solution.get_value(days))
            solutions.append(solution)

        pheromones = update_pheromones(solutions, pheromones, evaporation_rate,days)

        current_best_solution = max(solutions, key=lambda sol: sol.get_value(days))
        if current_best_solution.get_value(days)[0] > best_score:
            best_solution = current_best_solution
            best_score = current_best_solution.get_value(days)[0]

        print(current_best_solution.get_value(days)[0])

    return best_solution

# --- Helper Functions --- #

def initialize_pheromones(libraries, initial_pheromone):
    # Create a pheromone matrix 
    return [[initial_pheromone for _ in libraries] for _ in libraries]

def calculate_heuristic(library, book_scores, days, current_day):
    avg_book_score = sum(book_scores[book] for book in library.books) / len(library.books)
    potential_score = avg_book_score * (days - current_day - library.signup_time) * library.books_per_day
    return potential_score / library.signup_time  # Prioritize potential score considering signup cost


def calculate_probabilities(libraries, pheromones, book_scores, days, current_day, alpha, beta):
    probabilities = []

    for library in libraries:
        # Heuristic: (Change this to your desired heuristic calculation)
        heuristic_value = calculate_heuristic(library, book_scores, days, current_day)

        # Combine pheromone and heuristic
        combined_influence = (pheromones[library.id][library.id] ** alpha) * (heuristic_value ** beta)
        probabilities.append(combined_influence)

    # Normalize probabilities
    total_influence = sum(probabilities)
    if total_influence > 0:  # Prevent division by zero
        probabilities = [prob / total_influence for prob in probabilities]
    else:
        probabilities = [1/len(libraries) for _ in libraries]  # Default to equal probability if there's no guiding information 

    return probabilities



def construct_solution(libraries, book_scores, days, pheromones, alpha, beta):
    solution = classes.State([],{},book_scores,[],days)

    current_day = 0
    scanned_books = set()
    available_libraries = libraries.copy()

    while current_day < days and available_libraries:
        # Filtering: Find libraries that actually fit
        fitting_libraries = [lib for lib in available_libraries if current_day + lib.signup_time < days]

        if fitting_libraries: 
            probabilities = calculate_probabilities(fitting_libraries, pheromones, book_scores, days, current_day, alpha, beta)
            next_library = random.choices(fitting_libraries, weights=probabilities)[0]

            # Check if adding this library would exceed the total days
            if current_day + next_library.signup_time >= days:
                break

            current_day += next_library.signup_time
            solution.library_explored.append(next_library)

            scannable_books = [book for book in next_library.books if book not in scanned_books]
            scannable_books.sort(key=lambda book_id: book_scores[book_id], reverse=True)

            num_books_to_scan = min(len(scannable_books), (days - current_day) * next_library.books_per_day)
            solution.books_explored[next_library.id] = scannable_books[:num_books_to_scan]

            scanned_books.update(scannable_books[:num_books_to_scan])
            available_libraries.remove(next_library) 

        else: 
            break
    return solution

def update_pheromones(solutions, pheromones, evaporation_rate,days):
    # Local Pheromone Update (for all ants)
    for solution in solutions:
        for i in range(len(solution.library_explored) - 1):
            lib_1 = solution.library_explored[i]
            lib_2 = solution.library_explored[i + 1]
            pheromones[lib_1.id][lib_2.id] *= (1 - evaporation_rate)  # Evaporation first
            pheromones[lib_1.id][lib_2.id] += 1 / solution.get_value(days)[0]  # Smaller score means stronger reinforcement

    # Global Pheromone Update (by the best solution)
    best_solution = max(solutions, key=lambda sol: sol.get_value(days))
    for i in range(len(best_solution.library_explored) - 1):
        lib_1 = best_solution.library_explored[i]
        lib_2 = best_solution.library_explored[i + 1]
        pheromones[lib_1.id][lib_2.id] *= (1 - evaporation_rate)  
        pheromones[lib_1.id][lib_2.id] += 10 / best_solution.get_value(days)[0] # Stronger reinforcement for the best path

    return pheromones



