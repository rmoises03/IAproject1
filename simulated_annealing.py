import utils
import random
import math

def add_books_to_library_random(state, days, libraries):
    neighbors = []
    new_state_add_bookUnexplored = state.copy()
    if new_state_add_bookUnexplored.library_explored:
        # Vamos escolher uma library aleatoria já explorada: 
        library = random.choice(new_state_add_bookUnexplored.library_explored)
        # Vamos escolher um livro aleatorio da library escolhida que nao esteja na lista de livros explorados
        unexplored_books = [book for book in library.books if not utils.check_values_from_dict(new_state_add_bookUnexplored.books_explored, book)]
        if unexplored_books:
            book = random.choice(unexplored_books)
            new_state_add_bookUnexplored.books_explored.setdefault(library.id, []).append(book)
            if new_state_add_bookUnexplored.check_constraints(days):
                neighbors.append(new_state_add_bookUnexplored)
    return neighbors
        
def remove_book_from_library_random(state,days,libraries):
    neighbors = []
    new_state_remove_bookExplored = state.copy()
    #Vamos verificar se a lista de livros explorados nao esta vazia 
    non_empty_keys = [key for key, value in new_state_remove_bookExplored.books_explored.items() if value]
    # Vamos escolher um livro aleatorio dos que já foram explorados:
    if non_empty_keys != []:
        library_id = random.choice(non_empty_keys)
        # Vamos escolher um livro aleatorio da library escolhida
        book = random.choice(new_state_remove_bookExplored.books_explored[library_id])
        # Vamos remover esse livro e verificar se o nosso estado ainda é valido 
        new_state_remove_bookExplored.books_explored[library_id].remove(book)
        if new_state_remove_bookExplored.check_constraints(days):
            neighbors.append(new_state_remove_bookExplored)
            return neighbors
    
def add_library_to_signing_random(state,days,libraries):
    neighbors = []
    new_state_add_librarySigning = state.copy()
    if new_state_add_librarySigning.library_signing == [] and len(new_state_add_librarySigning.library_explored) != len(libraries) :
        # Vamos escolher uma library aleatoria que ainda nao foi explorada e que nao esteja na lista de libraries_signing
        library = random.choice([lib for lib in libraries if not utils.check_libraryExplored(new_state_add_librarySigning,lib) and not utils.check_librarySigning(new_state_add_librarySigning,lib)])
        if new_state_add_librarySigning.library_signing == []:
            new_state_add_librarySigning.library_signing = [library]
            if new_state_add_librarySigning.check_constraints(days):
                available_days = 0
                total_days_spend_on_signup = 0
                if(new_state_add_librarySigning.library_explored != []):
                    for library in new_state_add_librarySigning.library_explored:
                        total_days_spend_on_signup += library.signup_time
                        available_days = new_state_add_librarySigning.current_day - total_days_spend_on_signup
                        if available_days > 0 and available_days > new_state_add_librarySigning.library_signing[0].signup_time: 
                            neighbors.append(new_state_add_librarySigning)
                            return neighbors
                elif(new_state_add_librarySigning.library_explored == []):
                    neighbors.append(new_state_add_librarySigning)
                    return neighbors
                
def remove_library_from_explored_random(state,days,libraries):
    neighbors = []
    new_state_remove_libraryExplored = state.copy()
    counter = 0
    if new_state_remove_libraryExplored.library_explored != []: 
        # Vamos escolher uma library aleatoria que ja foi explorada
        library = random.choice(new_state_remove_libraryExplored.library_explored)
        new_state_remove_libraryExplored.library_explored.remove(library)
        new_state_remove_libraryExplored.books_explored[library.id] = []
        if new_state_remove_libraryExplored.check_constraints(days):
            neighbors.append(new_state_remove_libraryExplored)
            return neighbors
        

def remove_library_from_signing(state,days,libraries):
    neighbors = []
    new_state_remove_librarySigning = state.copy()
    if new_state_remove_librarySigning.library_signing:
        library_to_append = new_state_remove_librarySigning.library_signing[0]
        new_state_remove_librarySigning.library_explored.append(library_to_append)
        new_state_remove_librarySigning.library_signing = []
        # Permite-nos verificar se já passou tempo suficiente para que a library seja explorada
        if new_state_remove_librarySigning.check_constraints(days):
            neighbors.append(new_state_remove_librarySigning)
    return neighbors


def calculate_initial_temperature(state, days, libraries):
    modified_state = state.copy()
    neighbors = add_books_to_library_random(modified_state, days, libraries)
    if not neighbors: 
        raise ValueError("No neighbors found. Restarting...")
    sample_deltas = []
    for neighbor in neighbors:
        delta = neighbor.get_value(days)[0] - state.get_value(days)[0]
        sample_deltas.append(delta)

    if not sample_deltas:
        raise ValueError("No sample deltas found. Restarting...")

    avg_delta = sum(sample_deltas) / len(sample_deltas)

    return -avg_delta / math.log(0.8)

def update_temperature(temperature,cooling_rate):
    return temperature * cooling_rate


def simulated_annealing(initial_state, days, libraries,cooling_rate,max_iterations,stop_temperature):
    current_state = initial_state
    current_temp = calculate_initial_temperature(current_state,days,libraries)
    no_improvement_count = 0
    best_score = -float("inf")
    while True:
        neighbor_functions = [add_books_to_library_random, remove_book_from_library_random, add_library_to_signing_random, remove_library_from_explored_random, remove_library_from_signing]
        selected_functions = random.sample(neighbor_functions, 3)
        neighbors = [func(current_state,days,libraries) for func in selected_functions]
        neighbors = [neighbor for neighbor_list in neighbors for neighbor in (neighbor_list or [])]
        #Vamos querer parar quando a temperatura esta perto do 0 
        if current_state.get_value(days)[0] > best_score and current_state.check_constraints(days):
            best_score = current_state.get_value(days)[0]
            no_improvement_count = 0
        else:
            no_improvement_count += 1
        if current_temp <= stop_temperature or no_improvement_count >= max_iterations:
            return current_state
        if neighbors: 
            new_state = random.choice(neighbors) 
            delta_value = new_state.get_value(days)[0] - current_state.get_value(days)[0]
            if delta_value > 0: 
                current_state = new_state
            else: 
                try:
                    acceptance_probability = min (1, math.exp(delta_value / current_temp))
                except OverflowError:
                    acceptance_probability = 1  # As vezes o valor de delta_value é muito grande e causa overflow
                if random.random() < acceptance_probability:
                    current_state = new_state
            current_temp = update_temperature(current_temp,cooling_rate)
