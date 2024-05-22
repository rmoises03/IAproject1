import utils
import numpy as np

def add_books_to_library_heuristic(state, days, libraries):
    neighbors = []
    new_state_add_bookUnexplored = state.copy()
    new_state_add_bookUnexplored.library_explored.sort(key=lambda library: utils.library_score(library, new_state_add_bookUnexplored.book_scores, new_state_add_bookUnexplored.current_day), reverse=True)
    # Convert books_explored to a set for faster membership checking
    explored_books_set = {book for books in new_state_add_bookUnexplored.books_explored.values() for book in books}
    for library_explored in new_state_add_bookUnexplored.library_explored:
        # Use the set for membership checking instead of the dictionary
        unexplored_books = [book for book in library_explored.books if book not in explored_books_set]
        unexplored_books.sort(key=lambda book: new_state_add_bookUnexplored.book_scores[book], reverse=True)
        for unexplored_book in unexplored_books:
            new_state = new_state_add_bookUnexplored.copy() 
            new_state.books_explored.setdefault(library_explored.id, []).append(unexplored_book)
            if new_state.check_constraints(days):
                neighbors.append(new_state)
    return neighbors

def remove_book_from_library_heuristic(state, days, libraries):
    neighbors = []
    new_state_remove_bookExplored = state.copy()
    # Get all explored books and remove the one with the lowest score
    explored_books_set = np.array([book for books in new_state_remove_bookExplored.books_explored.values() for book in books])
    scores = np.array([new_state_remove_bookExplored.book_scores[book] for book in explored_books_set])
    sorted_indices = np.argsort(scores)
    # Remove the book with the lowest score and find it in the dictionary of explored books
    for index in sorted_indices:
        book = explored_books_set[index]
        new_state_remove_bookExplored = state.copy()
        for library_id, books in new_state_remove_bookExplored.books_explored.items():
            if book in books:
                books.remove(book)
                if new_state_remove_bookExplored.check_constraints(days):
                    neighbors.append(new_state_remove_bookExplored)

    return neighbors

def add_library_to_signing_heuristic(state,days,libraries):
    neighbors = []
    new_state_add_librarySigning = state.copy()
    #Vamos escolher a library com maior pontuação
    unexplored_libraries = [library for library in libraries if not utils.check_libraryExplored(new_state_add_librarySigning,library) and not utils.check_librarySigning(new_state_add_librarySigning,library)]
    unexplored_libraries.sort(key=lambda library: utils.library_score(library, new_state_add_librarySigning.book_scores, new_state_add_librarySigning.current_day), reverse=True)
    for library in unexplored_libraries:
        if new_state_add_librarySigning.library_signing == [] and len(new_state_add_librarySigning.library_explored) != len(libraries) :
            new_state_add_librarySigning.library_signing = [unexplored_libraries[0]]
            total_days_spend_on_signup = 0
            total_days_spend_on_signup = sum(library.signup_time for library in new_state_add_librarySigning.library_explored)
            if new_state_add_librarySigning.check_constraints(days) and new_state_add_librarySigning.current_day > library.signup_time + total_days_spend_on_signup:
                neighbors.append(new_state_add_librarySigning)
    return neighbors

def remove_library_from_explored_heuristic(state,days,libraries): 
    neighbors = []
    new_state_remove_libraryExplored = state.copy() 
    # Vamos escolher a library com menor pontuação
    if new_state_remove_libraryExplored.library_explored != []: 
        new_state_remove_libraryExplored.library_explored.sort(key = lambda library: utils.library_score(library, new_state_remove_libraryExplored.book_scores, new_state_remove_libraryExplored.current_day), reverse=False)
        for library in new_state_remove_libraryExplored.library_explored:
            new_state_remove_libraryExplored.library_explored.remove(library)
            if new_state_remove_libraryExplored.check_constraints(days):
                neighbors.append(new_state_remove_libraryExplored)
    return neighbors


def remove_library_from_signing_heuristic(state,days,libraries):
    neighbors = []
    new_state_remove_librarySigning = state.copy() 
    if new_state_remove_librarySigning.library_signing != []:
        new_state_remove_librarySigning.library_explored.append(new_state_remove_librarySigning.library_signing[0])
        new_state_remove_librarySigning.library_signing = []
        # Permite-nos verificar se já passou tempo suficiente para que a library seja explorada
        if (new_state_remove_librarySigning.check_constraints(days)):
            neighbors.append(new_state_remove_librarySigning)

    return neighbors


def tabu_search(initial_state,tabu_size,max_iterations,libraries):
    current_solution = initial_state.copy()
    best_solution = initial_state.copy()
    tabu_list = [current_solution]

    for _ in range(max_iterations):
        neighbors = []
        heuristics = [add_books_to_library_heuristic, remove_book_from_library_heuristic, add_library_to_signing_heuristic, remove_library_from_explored_heuristic, remove_library_from_signing_heuristic]

        for heuristic in heuristics:
            result = heuristic(current_solution, current_solution.current_day, libraries)
            if result is not None:
                neighbors += result

        if not neighbors:
            break

        next_solution = max(neighbors, key=lambda neighbor: neighbor.get_value(current_solution.current_day))

        tabu_list.append(next_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        current_solution = next_solution
        if current_solution.get_value(current_solution.current_day) > best_solution.get_value(best_solution.current_day):
            best_solution = current_solution
            print(best_solution.get_value(best_solution.current_day))
            

    return best_solution