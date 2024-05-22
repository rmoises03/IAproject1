# Problem Statements : 

## Given a set of L libraries with :

    N books; 
    T days required for signup; 
    M Books that can be shipped per day (after the signup process is done); 


## Objective : 

    Maximize the number of books that can be scanned before Time is over; 


## Constraints : 

    Each library can only be scanned/signup once; 
    The scan of the books can only be done after the library signup; 
    The amount of books that we can ship per day is defined for each library; 

## Optimization function: 

### Heuristic Library Score: 
    We will assign to each library a pontuation: 
        - The pontuation is calculated by the following : 
            1 - The books are first organized by descending order of their score; 
            2 - Calculate the number of books that are possible to read in the D days; 
            3 - Get the number of books that can be read in the possible days;
            4 - Calculate the total score of the books that can be read; 
            5 - Calculate the average score per day it takes to sign up the library

### Heuristic SignUp Time: 
    We will order the libraries for their signup time by ascending order.


## State Representation : [LE,BE,LS,D,BS] where : 
            LE -> Libraries Explored ; 
            BE -> Books Explored per Library; 
            LS -> Library in signing; 
            D -> Days left; 
            BS -> Book Scores 


## Initial State Representation : 
            State([], [], book_scores, [], days) where : 
                  libraries_explored = [] ; 
                  books_explored = []; 
                  book_scores = book_scores (passed as an argument); 
                  libraries_signing = []; 
                  days = days(passed as an argument); 



## Setup

* **Python Version:** This project was developed using Python 3.10.12. For best results, use the same version.

* **Required Packages:** Install the following packages using `pip`:

   ```bash
   pip install chain numpy
   ```

## Usage 

After the Setup is done you are ready to run the application, so inside the Project folder please run the main.py file.

```bash
python main.py
```

## Code Structure

Each Algorithm is in a separated file for easier modification and readability. 

### Utils 

In this file we have all the auxiliary functions that are needed to run the algorithms.
- Example: 

```python3

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


```

### Classes 

As the name mentions we used this file to store all the information related to the classes implemented in the project. 
- Example:

```python3

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
        # Check if the actual day < total days 
        if(self.current_day < 0 or self.current_day > days):
            return False
        
        # Check if the libraries explored doesn't exceed the number of days 
        if self.library_explored and sum(library.signup_time for library in self.library_explored) >= self.current_day:
            return False
        
        # Check Duplicates 
        if self.books_explored:
            all_books = [book for book_list in self.books_explored.values() for book in book_list]
            if len(all_books) != len(set(all_books)):
                return False

        # Check if the number of books explored doesn't exceed the the number of days * number of books per day
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

```

### Hill Climbing 

This algorithm compared to others has more disadvantages than advantages because it is computationally expensive and can get stuck easily. 

- Algorithms:
    - Hill Climbing Best Accept
    - Hill Climbing First Accept
    
- Operators:
    - Add_Books_To_Library
    - Remove_Books_From_Library
    - Add_Library_To_Signing
    - Remove_Library_To_Signing
    - Remove_Library_From_Explored.

 - Implementation:
```python3
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
```

### Simulated Annealing 

- Algorithms:
    - Simulated Annealing

- Operators:
    - Add_Books_To_Library_Random
    - Remove_Books_From_Library_Random
    - Add_Library_To_Signing_Random
    - Remove_Library_To_Signing_Random
    - Remove_Library_From_Explored_Random

- Auxiliary Functions:
    - Calculate_Initial_Temperature
    - Update_Temperature

- Implementation: 
```python3
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
```

### Tabu Search

- Algorithms:
    - Tabu Search
    - Tabu Search Limited

- Operators:
    - Add_Books_To_Library_Heuristic 
    - Remove_Books_From_Library_Heuristic
    - Add_Library_To_Signing_Heuristic
    - Remove_Library_To_Signing_Heuristic
    - Remove_Library_From_Explored_Heuristic

- Implementation: 
```python3


def tabu_search(initial_state,tabu_size,max_iterations,libraries,limited):
    current_solution = initial_state.copy()
    best_solution = initial_state.copy()
    tabu_list = [current_solution]
    for _ in range(max_iterations):
        neighbors = []
        if(limited == 0):
            heuristics = [add_books_to_library_heuristic, remove_book_from_library_heuristic, add_library_to_signing_heuristic, remove_library_from_explored_heuristic, remove_library_from_signing_heuristic]
            for heuristic in heuristics:
                result = heuristic(current_solution, current_solution.current_day, libraries)
                if result is not None:
                    neighbors += result
        
        else:
            heuristics = [add_books_to_library_heuristic_limited, remove_book_from_library_heuristic_limited, add_library_to_signing_heuristic_limited, remove_library_from_explored_heuristic_limited, remove_library_from_signing_heuristic_limited]
            for heuristic in heuristics:
                result = heuristic(current_solution, current_solution.current_day, libraries,limited)
                if result is not None:
                    neighbors += result
        if not neighbors:
            break

        # Filter out neighbors that are in the tabu_list
        non_tabu_neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]
        
        if not non_tabu_neighbors:
            next_solution = max(neighbors, key=lambda neighbor: neighbor.get_value(current_solution.current_day))
        else:
            next_solution = max(non_tabu_neighbors, key=lambda neighbor: neighbor.get_value(current_solution.current_day))

        tabu_list.append(next_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        current_solution = next_solution
        if current_solution.get_value(current_solution.current_day) > best_solution.get_value(best_solution.current_day):
            best_solution = current_solution

    return best_solution

```

### Genetic Algorithm

- Algorithms:
    - Genetic Algorithm

- Operators:
    - Add_Books_To_Library
    - Remove_Books_From_Library
    - Add_Library_To_State
    - Remove_Library_From_Explored

- Auxiliary Functions:
    - Ordered Crossover
    - Tournment Selection
    - Roulette Selection
    - Swap Mutation

- Implementation:
```python3
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
```

### Ant Colony 

- Algorithms:
    - Ant Colony 

- Auxiliary Functions:
    - Construct Solution
    - Update Pheromones
    - Calculate Probabilities 
    - Calculate Heuristic
    - Initialize Pheromones

- Implementation:
```python3
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

``` 


 











