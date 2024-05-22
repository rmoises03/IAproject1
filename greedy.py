import numpy as np
import utils


def greedy_solution(state, libraries, book_scores, days):
    state.library_signing = libraries.pop(0)
    state.current_day += state.library_signing.signup_time
    state.library_explored.append(state.library_signing)
    state.library_signing = []
    total_score = 0

    while state.current_day < days:
        if not state.library_signing and libraries:  # More concise condition
            state.library_signing = libraries.pop(0)

        if state.library_signing:
            if state.library_signing.signup_time == 0:
                state.library_explored.append(state.library_signing)
                state.library_signing = []

        if state.current_day > days:
            break

        lib_scores = [utils.library_score(lib, book_scores, days) for lib in state.library_explored]
        order = sorted(range(len(lib_scores)), key=lambda k: lib_scores[k], reverse=True)

        for k_idx in order:
            k = state.library_explored[k_idx]

            books_to_scan = min(k.books_per_day, len(k.books))
            potential_scans = k.books[:books_to_scan]
            k.books = k.books[books_to_scan:]

            explored_books = list(set([book for lib in state.books_explored.values() for book in lib]))

            valid_scans = [book for book in potential_scans if book not in explored_books]

            state.books_explored[k.id] = state.books_explored.get(k.id, []) + valid_scans

            total_score += sum([book_scores[book_id] for book_id in valid_scans])

        state.current_day += 1
        if state.library_signing:
            state.library_signing.signup_time -= 1

    state.library_signing = [state.library_signing] if state.library_signing else []

    return state