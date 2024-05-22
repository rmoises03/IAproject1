import utils 
import random 
import numpy as np
import classes
from itertools import islice


def roulette_selection(population):
    # Calculate the total fitness of the population
    total_fitness = sum(state.get_value(state.current_day)[0] for state in population if state.check_constraints(state.current_day))

    # Generate a random number between 0 and the total fitness
    rand_num = random.uniform(0, total_fitness)

    # Initialize the cumulative sum
    cumulative_sum = 0

    # Go through the population
    for state in population:
        # Add the fitness of the individual to the cumulative sum
        if state.check_constraints(state.current_day):
            cumulative_sum += state.get_value(state.current_day)[0]

        # If the cumulative sum is greater than or equal to the random number, return the individual
        if cumulative_sum >= rand_num:
            return state

    # In case no feasible individual is found, return a random individual
    return random.choice(population)


def tournament_selection(population, tournament_size):
    while True:
        # Randomly select tournament_size individuals from the population
        tournament = random.sample(population, tournament_size)

        # Select the individual with the highest fitness
        winner = max(tournament, key=lambda state: state.get_value(state.current_day)[0])
        
        if(winner.check_constraints(winner.current_day)):
            return winner

def ordered_crossover(parent1, parent2): 
        size = min(len(parent1.library_explored), len(parent2.library_explored))

        counter = 0

        # Ensure there are at least two genes for crossover
        if size < 2:
            return parent1, parent2
        feasible_children = False
        while not feasible_children or counter == 50: 
            # Generate a random range within which genes from parent1 will be copied to the child
            start, end = sorted(random.sample(range(size), 2))

            # Initialize children
            child1 = classes.State(library_explored=[]*size, books_explored={}, book_scores=parent1.book_scores, library_signing=[], current_day=parent1.current_day)
            child2 = classes.State(library_explored=[]*size, books_explored={}, book_scores=parent2.book_scores, library_signing=[], current_day=parent1.current_day)

            # Fill the remaining genes with the genes from the other parent in the order they appear
            i = 0
            while i < size:
                if parent2.library_explored[i] not in child1.library_explored:
                    child1.library_explored.append(parent2.library_explored[i])
                    child1.books_explored[parent2.library_explored[i].id] = parent1.books_explored.get(parent2.library_explored[i].id, []).copy()
                    child1.book_scores = parent2.book_scores
                if parent1.library_explored[i] not in child2.library_explored:
                    child2.library_explored.append(parent1.library_explored[i])
                    child2.books_explored[parent1.library_explored[i].id] = parent2.books_explored.get(parent1.library_explored[i].id, []).copy()
                    child2.book_scores = parent1.book_scores
                i += 1

            # Check feasibility
            if child1.check_constraints(child1.current_day) and child2.check_constraints(child2.current_day):
                feasible_children = True  
            counter += 1          

            return child1, child2
        return 0,0
        


def add_book_to_library(state, libraries):
    counter = 0
    while counter != 50:   
        unexplored = utils.get_unexplored_books(libraries, state.books_explored)
        #Select a random book from the tuples (book,library) 
        unexplored_tuple = random.choice(unexplored)
        mutated_state = state.copy()
        mutated_state.books_explored.setdefault(unexplored_tuple[1], []).append(unexplored_tuple[0])
        counter+=1
        if mutated_state.check_constraints(mutated_state.current_day):
            return (mutated_state,0)
    return (state,1)
                 

def remove_book_to_library(state,libraries): 
    counter = 0
    while counter != 50: 
        mutated_state = state.copy()
        # Get a book already explored and remove it 
        libraries_with_books = [library for library in mutated_state.books_explored.keys() if mutated_state.books_explored != []]
        if libraries_with_books:
            library = random.choice(libraries_with_books)
            if mutated_state.books_explored[library] != []:
                book = random.choice(mutated_state.books_explored[library])
                mutated_state.books_explored[library].remove(book)
                counter += 1
                if mutated_state.check_constraints(mutated_state.current_day):
                    return (mutated_state,0)
    return (state,1)

def add_library_to_state(state,libraries): 
    counter = 0
    while counter != 50:
        # Add a library unexplored to the state 
        mutated_state = state.copy()
        library = random.choice(libraries)
        mutated_state.library_explored.append(library)
        counter += 1
        if mutated_state.check_constraints(mutated_state.current_day):
            return (mutated_state,0)
    return (state,1)

def remove_library_to_state(state,libraries): 
    counter = 0
    while counter != 50: 
        # Remove a library already explored 
        mutated_state = state.copy()
        library = random.choice(mutated_state.library_explored)
        mutated_state.library_explored.remove(library)
        counter += 1
        if mutated_state.check_constraints(mutated_state.current_day):
            return (mutated_state,0)
    return (state,1)
        
        
def swap_mutation(mutated_state, libraries):
    # Initialize the list of heuristics
    heuristics = []
    while True: 
        # Check if there are any more libraries to add  
        if(len(mutated_state.library_explored) + len(mutated_state.library_signing) < len(libraries)):
            heuristics.append(add_library_to_state)

        # Check if there are any books to add
        if utils.get_unexplored_books(libraries, mutated_state.books_explored):
            heuristics.append(add_book_to_library)
        
        # Check if there are any libraries to remove 
        if mutated_state.library_explored:
            heuristics.append(remove_library_to_state)

        # Check if there are any books to remove
        if any(mutated_state.books_explored.values()):
            heuristics.append(remove_book_to_library)

        # Randomly select a function
        heuristic = random.choice(heuristics)

        # Apply the selected function
        mutated_state,check = heuristic(mutated_state, libraries)

        if check != 1:
            return mutated_state


def random_mutation(mutated_state):
    if len(mutated_state.library_explored) >= 2:
        # Randomly select an index for mutation
        i = random.randint(0, len(mutated_state.library_explored) - 1)

        # Randomly select a new library for mutation
        new_library = random.choice(list(mutated_state.books_explored.keys()))

        # Replace the selected library with the new library
        mutated_state.library_explored[i] = new_library

    return mutated_state

def genetic_algorithm(population, days, num_generations, tournament_size, mutation_rate,libraries, selected):
    for _ in range(num_generations):
        new_population = []

        # Elitism: keep the best individuallibraries
        population.sort(key=lambda state: state.get_value(days)[0], reverse=True)
        new_population.append(population[0])

        while len(new_population) < len(population):
            if selected == 1:
                # Selection by tournament
                parent1 = tournament_selection(population, tournament_size)
                parent2 = tournament_selection(population, tournament_size)
            else:
                # Selection by roulette
                parent1 = roulette_selection(population)
                parent2 = roulette_selection(population)

            # Crossover
            child1, child2 = ordered_crossover(parent1, parent2)

            while child1 == 0 and child2 == 0: 
                parent1 = roulette_selection(population)
                parent2 = roulette_selection(population)
                child1, child2 = ordered_crossover(parent1, parent2)
            
            # Mutation
            if np.random.rand() < mutation_rate: 
                child1 = swap_mutation(child1,libraries)
                # child1 = random_mutation(child1)
                if not child1.check_constraints(days):  # Check feasibility
                    continue  # Discard child1 if not feasible
            if np.random.rand() < mutation_rate:
                child2 = swap_mutation(child2,libraries)
                # child2 = random_mutation(child2)
                if not child2.check_constraints(days):  # Check feasibility
                    continue  # Discard child2 if not feasible

            new_population.extend([child1, child2])
            

        for k in range(len(new_population)): 
                best = 0
                best = utils.get_values_from_dict(new_population[k].books_explored,new_population[k].book_scores)
        population = new_population
        
    # Return the best solution
    population.sort(key=lambda state: state.get_value(days)[0], reverse=True)
    return population[0]