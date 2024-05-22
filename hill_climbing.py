import utils
import keyboard

def add_books_to_library(state,days,libraries):
    neighbors = []
    new_state_add_bookUnexplored = state.copy()
    for library in state.library_explored:
        for book in library.books:
            # Se o livro ainda nao estiver na lista de livros explorados
            new_state_add_bookUnexplored = state.copy()
            books_explored_set = {book for books in new_state_add_bookUnexplored.books_explored.values() for book in books}
            if book not in books_explored_set:
                new_state_add_bookUnexplored.books_explored.setdefault(library.id, []).append(book)
                if new_state_add_bookUnexplored.check_constraints(days):
                    neighbors.append(new_state_add_bookUnexplored)

    return neighbors

def remove_book_from_library(state,days,libraries):
    neighbors = []
    new_state_remove_bookExplored = state.copy()
    for library in new_state_remove_bookExplored.library_explored:
        for book in library.books:
            new_state_remove_bookExplored = state.copy()
            if(utils.check_values_from_dict_withLibrary(new_state_remove_bookExplored.books_explored,book,library.id) == True):
                new_state_remove_bookExplored.books_explored[library.id].remove(book)
                if new_state_remove_bookExplored.check_constraints(days):
                    neighbors.append(new_state_remove_bookExplored)

    return neighbors


def swap_books_from_libraries(state,days,libraries):
    neighbors = []
    new_state = state.copy()
    for lib1 in new_state.library_explored:
        for lib2 in new_state.library_explored:
            #Caso em que elas são iguais
            if lib1 == lib2:
                continue
            if lib1.id in new_state.books_explored and lib2.id in new_state.books_explored:
                for book1 in range(len(new_state.books_explored[lib1.id])):
                    for book2 in range(len(new_state.books_explored[lib2.id])):
                        new_state = state.copy()
                        new_state.books_explored[lib1.id][book1], new_state.books_explored[lib2.id][book2] = \
                            new_state.books_explored[lib2.id][book2], new_state.books_explored[lib1.id][book1]
                        if new_state.check_constraints(days):
                            neighbors.append(new_state)

    return neighbors

def add_library_to_signing(state,days,libraries):
    neighbors = []
    new_state_add_librarySigning = state.copy()
    for library in libraries:
        if not utils.check_libraryExplored(new_state_add_librarySigning, library) and not utils.check_librarySigning(new_state_add_librarySigning, library):
            if not new_state_add_librarySigning.library_signing:
                new_state_add_librarySigning.library_signing = [library]
                if new_state_add_librarySigning.check_constraints(days):
                    total_days_spend_on_signup = sum(lib.signup_time for lib in new_state_add_librarySigning.library_explored)
                    available_days = new_state_add_librarySigning.current_day - total_days_spend_on_signup
                    signup_time = new_state_add_librarySigning.library_signing[0].signup_time
                    if available_days > 0 and available_days > signup_time: 
                        neighbors.append(new_state_add_librarySigning)
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


def remove_library_from_explored(state,days,libraries):
    neighbors = []
    if state.library_explored:
        for counter, library in enumerate(state.library_explored):
            new_state_remove_libraryExplored = state.copy()
            new_state_remove_libraryExplored.library_explored = state.library_explored.copy()
            new_state_remove_libraryExplored.library_explored.pop(counter)
            new_state_remove_libraryExplored.books_explored[library.id] = []
            if new_state_remove_libraryExplored.check_constraints(days):
                neighbors.append(new_state_remove_libraryExplored)
    return neighbors


def add_books_to_library_accept(state,days,libraries):
    neighbors = []
    new_state_add_bookUnexplored = state.copy()
    for library in state.library_explored:
        for book in library.books:
            # Se o livro ainda nao estiver na lista de livros explorados
            new_state_add_bookUnexplored = state.copy()
            books_explored_set = {book for books in new_state_add_bookUnexplored.books_explored.values() for book in books}
            if book not in books_explored_set:
                new_state_add_bookUnexplored.books_explored.setdefault(library.id, []).append(book)
                if new_state_add_bookUnexplored.check_constraints(days):
                    neighbors.append(new_state_add_bookUnexplored)
                    return neighbors 
                
    return neighbors

def remove_book_from_library_accept(state,days,libraries):
    neighbors = []
    new_state_remove_bookExplored = state.copy()
    for library in new_state_remove_bookExplored.library_explored:
        for book in library.books:
            new_state_remove_bookExplored = state.copy()
            if(utils.check_values_from_dict_withLibrary(new_state_remove_bookExplored.books_explored,book,library.id) == True):
                new_state_remove_bookExplored.books_explored[library.id].remove(book)
                if new_state_remove_bookExplored.check_constraints(days):
                    neighbors.append(new_state_remove_bookExplored)
                    return neighbors

    return neighbors


def swap_books_from_libraries_accept(state,days,libraries):
    neighbors = []
    new_state = state.copy()
    for lib1 in new_state.library_explored:
        for lib2 in new_state.library_explored:
            #Caso em que elas são iguais
            if lib1 == lib2:
                continue
            if lib1.id in new_state.books_explored and lib2.id in new_state.books_explored:
                for book1 in range(len(new_state.books_explored[lib1.id])):
                    for book2 in range(len(new_state.books_explored[lib2.id])):
                        new_state = state.copy()
                        new_state.books_explored[lib1.id][book1], new_state.books_explored[lib2.id][book2] = \
                            new_state.books_explored[lib2.id][book2], new_state.books_explored[lib1.id][book1]
                        if new_state.check_constraints(days):
                            neighbors.append(new_state)
                            return neighbors

    return neighbors

def add_library_to_signing_accept(state,days,libraries):
    neighbors = []
    new_state_add_librarySigning = state.copy()
    for library in libraries:
        if not utils.check_libraryExplored(new_state_add_librarySigning, library) and not utils.check_librarySigning(new_state_add_librarySigning, library):
            if not new_state_add_librarySigning.library_signing:
                new_state_add_librarySigning.library_signing = [library]
                if new_state_add_librarySigning.check_constraints(days):
                    total_days_spend_on_signup = sum(lib.signup_time for lib in new_state_add_librarySigning.library_explored)
                    available_days = new_state_add_librarySigning.current_day - total_days_spend_on_signup
                    signup_time = new_state_add_librarySigning.library_signing[0].signup_time
                    if available_days > 0 and available_days > signup_time: 
                        neighbors.append(new_state_add_librarySigning)
                        return neighbors 
    return neighbors


def remove_library_from_signing_accept(state,days,libraries):
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
    return neighbors


def remove_library_from_explored_accept(state,days,libraries):
    neighbors = []
    if state.library_explored:
        for counter, library in enumerate(state.library_explored):
            new_state_remove_libraryExplored = state.copy()
            new_state_remove_libraryExplored.library_explored = state.library_explored.copy()
            new_state_remove_libraryExplored.library_explored.pop(counter)
            new_state_remove_libraryExplored.books_explored[library.id] = []
            if new_state_remove_libraryExplored.check_constraints(days):
                neighbors.append(new_state_remove_libraryExplored)
                return neighbors
    return neighbors


def hill_climbing(initial_state, days, libraries):
    current_state = initial_state
    while True:
        neighbors_add =  add_books_to_library(current_state, days, libraries)
        neighbors_remove = remove_book_from_library(current_state, days, libraries)
        neighbors_add_library = add_library_to_signing(current_state, days, libraries)
        neighbors_remove_library = remove_library_from_signing(current_state, days, libraries)
        neighbors_remove_library_explored = remove_library_from_explored(current_state, days, libraries)
        neighbors = neighbors_add + neighbors_remove  + neighbors_add_library + neighbors_remove_library + neighbors_remove_library_explored
        if neighbors:
            best_neighbor = max(neighbors, key=lambda neighbor: neighbor.get_value(days))
            if (current_state.get_value(days) > best_neighbor.get_value(days)):
                break
            current_state = best_neighbor
        else:
            if current_state.current_day > days:
                break
            current_state.current_day += 1

    return current_state


def hill_climbing_first_accept(initial_state, days, libraries):
    current_state = initial_state
    while True:
        neighbors_add =  add_books_to_library_accept(current_state, days, libraries)
        neighbors_remove = remove_book_from_library_accept(current_state, days, libraries)
        neighbors_add_library = add_library_to_signing_accept(current_state, days, libraries)
        neighbors_remove_library = remove_library_from_signing_accept(current_state, days, libraries)
        neighbors_remove_library_explored = remove_library_from_explored_accept(current_state, days, libraries)
        neighbors = neighbors_add + neighbors_remove  + neighbors_add_library + neighbors_remove_library + neighbors_remove_library_explored
        if neighbors:
            best_neighbor = max(neighbors, key=lambda neighbor: neighbor.get_value(days))
            if (current_state.get_value(days) > best_neighbor.get_value(days)):
                break
            current_state = best_neighbor
        else:
            if current_state.current_day > days:
                break
            current_state.current_day += 1

    return current_state




