import numpy as np
import random
import classes
import utils
from itertools import chain

def get_book_score(id,books_scores):
    return books_scores[id]

def get_values_from_dict(dictionary, book_scores):
    # Vamos usar a biblioteca numpy para obtermos melhor eficiencia 
    values = np.array([value for values_list in dictionary.values() for value in values_list])

    return np.sum([book_scores[id] for id in values.tolist()])


def check_values_from_dict(dictionary, value):
    for k in dictionary.values():
        if value in k:
            return True
    return False


def check_values_from_dict_withLibrary(dictionary, value, library_id):
    if library_id in dictionary:
        if value in dictionary[library_id]:
            return True
    return False

def check_values_from_dict_withLibrary1(dict, value):
    # Iterate over all items in the dictionary
    for books in dict.values():
        # If the value is in the list of books, return True
        if value in books:
            return True
    # If the value is not in any list of books, return False
    return False


def check_libraryExplored(state,library):
    for lib in state.library_explored:
        if lib.id == library.id:
            return True
    return False

def check_librarySigning(state,library):
    for lib in state.library_signing:
        if lib.id == library.id:
            return True
    return False
    
def library_score(library, book_scores, days):
    if not library.books:
        return 0

    if library.signup_time == 0:
        return np.sum([book_scores[book] for book in library.books])

    num_books_can_be_read = days * library.books_per_day
    books_to_be_read = library.books[:num_books_can_be_read]
    total_books_score = np.sum([book_scores[book] for book in books_to_be_read])
    average_score_per_day = total_books_score / library.signup_time

    return average_score_per_day

def get_unexplored_books(libraries, books_explored): 
    books = []
    explored_books = set(chain.from_iterable(books_explored.values()))
    for library in libraries:
        for book in library.books:
            if book not in explored_books:
                books.append((book, library.id))
    return books

def random_solution(libraries, book_scores, Days):
    random_libraries = []
    total_signup_time = 0

    # Select a random number of libraries until total signup time exceeds Days
    num_libraries = random.randint(0, len(libraries))
    for library in libraries[:num_libraries]:
        if total_signup_time + library.signup_time > Days:
            break
        random_libraries.append(library)
        total_signup_time += library.signup_time

    random_books = {}
    all_selected_books = set()

    remaining_days = Days
    for library in random_libraries:
        # Select books that haven't been selected yet
        available_books = set(library.books) - all_selected_books
        if not available_books:
            continue
        remaining_days -= library.signup_time
        max_books = remaining_days * library.books_per_day
        num_books = min(max_books, len(available_books))
        num_books = random.randint(0, num_books)  # Select a random number of books
        selected_books = set(random.sample(available_books, num_books))
        random_books[library.id] = list(selected_books)
        all_selected_books.update(selected_books)

    # Select a random library for random_signing from the remaining libraries
    remaining_libraries = [library for library in libraries if library not in random_libraries]
    random_signing = [random.choice(remaining_libraries)] if remaining_libraries else []

    return classes.State(library_explored=random_libraries, books_explored=random_books, book_scores=book_scores, library_signing=random_signing, current_day=Days)

def random_solution_per_signup(libraries, book_scores, Days):
    # Sort libraries by signup time in ascending order
    libraries_sorted = sorted(libraries, key=lambda x: x.signup_time)

    random_libraries = []
    total_signup_time = 0

    # Select a random number of libraries until total signup time exceeds Days
    num_libraries = random.randint(0, len(libraries_sorted))
    for library in libraries_sorted[:num_libraries]:
        if total_signup_time + library.signup_time > Days:
            break
        random_libraries.append(library)
        total_signup_time += library.signup_time

    random_books = {}
    all_selected_books = set()

    remaining_days = Days
    for library in random_libraries:
        # Select books that haven't been selected yet
        available_books = set(library.books) - all_selected_books
        if not available_books:
            continue
        remaining_days -= library.signup_time
        max_books = remaining_days * library.books_per_day
        num_books = min(max_books, len(available_books))
        num_books = random.randint(0, num_books)  # Select a random number of books
        selected_books = set(random.sample(available_books, num_books))
        random_books[library.id] = list(selected_books)
        all_selected_books.update(selected_books)

    # Select a random library for random_signing from the remaining libraries
    remaining_libraries = [library for library in libraries_sorted if library not in random_libraries]
    random_signing = [random.choice(remaining_libraries)] if remaining_libraries else []

    return classes.State(library_explored=random_libraries, books_explored=random_books, book_scores=book_scores, library_signing=random_signing, current_day=Days)

def readFile(file): 
    fileChosen = open("Project/inputs/" + file, "r")
    lines = fileChosen.readlines()

    Days = int(lines[0].split(' ')[2])
    book_scores = {i: int(score) for i, score in enumerate(lines[1].split())}

    libraries = []
    for counter, line in enumerate(lines[2:], start=0):
        if counter % 2 == 0:
            books, signup_time, books_per_day = map(int, line.split(' '))
        else: 
            books_in_the_library = list(map(int, line.split()))
            libraries.append(classes.Library(counter // 2, books_in_the_library, signup_time, books_per_day))

    return libraries, book_scores, Days

#Sort the books by their score in descending order
def sort_libraries_by_score(libraries,book_scores,Days):
    for library in libraries:
        library.books.sort(key=lambda book: book_scores[book], reverse=True)
    libraries.sort(key=lambda library: utils.library_score(library, book_scores, Days), reverse=True)
    return libraries
