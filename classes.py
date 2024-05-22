import utils

class Book: 
    def __init__(self, score):
        self.score = score

    def __str__(self):
        return f"{self.score}"

    def __repr__(self):
        return f"Book({self.score})"
    

class Library: 
    def __init__(self, id, books, signup_time, books_per_day):
        self.id = int(id)
        self.books = books
        self.signup_time = int(signup_time)
        self.books_per_day = int(books_per_day)

    def __str__(self):
        return f"{self.id} {self.books} {self.signup_time} {self.books_per_day}"

    def __repr__(self):
        return f"Library({self.id} {self.books} {self.signup_time} {self.books_per_day})"

    
class State:
    def __init__(self, library_explored, books_explored, book_scores, library_signing, current_day):
        self.current_day = int(current_day)
        self.book_scores = book_scores
        self.library_explored = library_explored
        self.library_signing = library_signing
        self.books_explored = books_explored

    def get_value(self, days):
        library_signing_bonus = 1 if self.library_signing != [] else 0
        if not self.check_constraints(days):
            return -float("inf"), -float("inf"), -float("inf"), 0
        else:
            return (
                utils.get_values_from_dict(self.books_explored, self.book_scores),
                len(self.library_explored),
                len(self.books_explored),
                library_signing_bonus
            )
    
    def copy(self):
        return State(
            self.library_explored[:], 
            {k: v[:] for k, v in self.books_explored.items() if self.books_explored != {}}, 
            self.book_scores, 
            self.library_signing,
            self.current_day
        )
    

    def check_constraints(self,days):
        # Vamos verificar se o actual day é menor do que os days que temos
        if(self.current_day < 0 or self.current_day > days):
            return False
        
        # Vamos verificar se as libraries explored nao excedem o tempo de dias que ja passaram 
        if self.library_explored and sum(library.signup_time for library in self.library_explored) >= self.current_day:
            return False
        
        # Vamos verificar se existem duplicados 
        if self.books_explored:
            all_books = [book for book_list in self.books_explored.values() for book in book_list]
            if len(all_books) != len(set(all_books)):
                return False

        # Vamos verificar se o numero de livros explorados é maior do que o numero de dias * numero de livros por dia
        if self.books_explored:
            remaining_days = self.current_day
            for library in self.library_explored:
                remaining_days -= library.signup_time
                if remaining_days < 0:
                    return False
                if library.id in self.books_explored:
                    if len(self.books_explored[library.id]) > remaining_days * library.books_per_day:
                        return False
        
        return True