import random
import math
import time
import numpy as np
import hill_climbing as hill
import utils
import simulated_annealing as sa
import tabu_search as ts
import genetic_algorithm as ga
import antcolony as ac
import classes





def main() : 
        
    try : 
        # # Hill Climbing 
        # libraries,book_scores,Days = utils.readFile("c_incunabula.txt")
        # initial_solution_random = utils.random_solution(libraries,book_scores,Days)
        # best_solution_from_hill_climbing = hill.hill_climbing_first_accept(initial_solution_random,Days,libraries)
        # total_score = utils.get_values_from_dict(best_solution_from_hill_climbing.books_explored,book_scores)
        # print("Hill Climbing: ", total_score)

        # Hill Climbing First Accept
        libraries,book_scores, Days = utils.readFile("a_example.txt")
        start_time = time.time()
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days) 
        best_solution_from_hill_climbing_first_accept = hill.hill_climbing_first_accept(initial_solution_random, Days,libraries) 
        total_score = utils.get_values_from_dict(best_solution_from_hill_climbing_first_accept.books_explored,book_scores)
        final_time = time.time() - start_time
        print("Time: ", final_time)
        print("Hill Climbing First Accept: ", total_score)

        # Hill Climbing First Accept
        libraries,book_scores, Days = utils.readFile("b_read_on.txt")
        start_time = time.time()
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days) 
        best_solution_from_hill_climbing_first_accept = hill.hill_climbing_first_accept(initial_solution_random, Days,libraries) 
        total_score = utils.get_values_from_dict(best_solution_from_hill_climbing_first_accept.books_explored,book_scores)
        final_time = time.time() - start_time
        print("Time: ", final_time)
        print("Hill Climbing First Accept: ", total_score)

        # Hill Climbing First Accept
        libraries,book_scores, Days = utils.readFile("c_incunabula.txt")
        start_time = time.time()
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days) 
        best_solution_from_hill_climbing_first_accept = hill.hill_climbing_first_accept(initial_solution_random, Days,libraries) 
        total_score = utils.get_values_from_dict(best_solution_from_hill_climbing_first_accept.books_explored,book_scores)
        final_time = time.time() - start_time
        print("Time: ", final_time)
        print("Hill Climbing First Accept: ", total_score)

        # Hill Climbing First Accept
        libraries,book_scores, Days = utils.readFile("d_tough_choices.txt")
        start_time = time.time()
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days) 
        best_solution_from_hill_climbing_first_accept = hill.hill_climbing_first_accept(initial_solution_random, Days,libraries) 
        total_score = utils.get_values_from_dict(best_solution_from_hill_climbing_first_accept.books_explored,book_scores)
        final_time = time.time() - start_time
        print("Time: ", final_time)
        print("Hill Climbing First Accept: ", total_score)

        # Hill Climbing First Accept
        libraries,book_scores, Days = utils.readFile("e_so_many_books.txt")
        start_time = time.time()
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days) 
        best_solution_from_hill_climbing_first_accept = hill.hill_climbing_first_accept(initial_solution_random, Days,libraries) 
        total_score = utils.get_values_from_dict(best_solution_from_hill_climbing_first_accept.books_explored,book_scores)
        final_time = time.time() - start_time
        print("Time: ", final_time)
        print("Hill Climbing First Accept: ", total_score)

        # Hill Climbing First Accept
        libraries,book_scores, Days = utils.readFile("f_libraries_of_the_world.txt")
        start_time = time.time()
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days) 
        best_solution_from_hill_climbing_first_accept = hill.hill_climbing_first_accept(initial_solution_random, Days,libraries) 
        total_score = utils.get_values_from_dict(best_solution_from_hill_climbing_first_accept.books_explored,book_scores)
        final_time = time.time() - start_time
        print("Time: ", final_time)
        print("Hill Climbing First Accept: ", total_score)


        # Simulated Annealing
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("a_example.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_simulated_annealing = sa.simulated_annealing(initial_solution_random,Days,libraries,0.99,1000000000,0.0000001)
        total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Simulated Annealing: ", total_score, " Time: ", end_time)

        # Simulated Annealing
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("b_read_on.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_simulated_annealing = sa.simulated_annealing(initial_solution_random,Days,libraries,0.99,1000000000,0.0000001)
        total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Simulated Annealing: ", total_score, " Time: ", end_time)

        # Simulated Annealing
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("c_incunabula.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_simulated_annealing = sa.simulated_annealing(initial_solution_random,Days,libraries,0.99,1000000000,0.0000001)
        total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Simulated Annealing: ", total_score, " Time: ", end_time)


        # Simulated Annealing
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("d_tough_choices.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_simulated_annealing = sa.simulated_annealing(initial_solution_random,Days,libraries,0.99,1000000000,0.0000001)
        total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Simulated Annealing: ", total_score, " Time: ", end_time)

        # Simulated Annealing
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("f_libraries_of_the_world.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_simulated_annealing = sa.simulated_annealing(initial_solution_random,Days,libraries,0.99,1000000000,0.0000001)
        total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Simulated Annealing: ", total_score, " Time: ", end_time)

        # Simulated Annealing
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("e_so_many_books.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_simulated_annealing = sa.simulated_annealing(initial_solution_random,Days,libraries,0.99,1000000000,0.0000001)
        total_score = utils.get_values_from_dict(best_solution_from_simulated_annealing.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Simulated Annealing: ", total_score, " Time: ", end_time)
        

        # Tabu Search
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("a_example.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_tabu_search = ts.tabu_search(initial_solution_random,10,100,libraries)
        total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Tabu Search: ", total_score, " Time: ", end_time)

        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("b_read_on.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_tabu_search = ts.tabu_search(initial_solution_random,10,100,libraries)
        total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Tabu Search: ", total_score, " Time: ", end_time)

        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("c_incunabula.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_tabu_search = ts.tabu_search(initial_solution_random,10,100,libraries)
        total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Tabu Search: ", total_score, " Time: ", end_time)

        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("d_tough_choices.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_tabu_search = ts.tabu_search(initial_solution_random,10,100,libraries)
        total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Tabu Search: ", total_score, " Time: ", end_time)

        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("f_libraries_of_the_world.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_tabu_search = ts.tabu_search(initial_solution_random,10,100,libraries)
        total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Tabu Search: ", total_score , " Time: ", end_time)

        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("e_so_many_books.txt")
        initial_solution_random = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_tabu_search = ts.tabu_search(initial_solution_random,10,100,libraries)
        total_score = utils.get_values_from_dict(best_solution_from_tabu_search.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Tabu Search: ", total_score, " Time: ", end_time)

        # Genetic Algorithm
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("a_example.txt")
        # Define the parameters for the genetic algorithm
        num_generations = 100  # Number of generations
        population_size = 50  # Size of population
        tournament_size = 20  # Size of tournament for tournament selection
        mutation_rate = 0.1  # Probability of mutation
        ## Create an initial population of random solutions
        population = [utils.random_solution_per_signup(libraries,book_scores,Days) for _ in range(population_size)]
        best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries,0)
        total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Genetic Algorithm: ", total_score, " Time: ", end_time)

        # Genetic Algorithm
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("b_read_on.txt")
        # Define the parameters for the genetic algorithm
        num_generations = 100  # Number of generations
        population_size = 50  # Size of population
        tournament_size = 20  # Size of tournament for tournament selection
        mutation_rate = 0.1  # Probability of mutation
        ## Create an initial population of random solutions
        population = [utils.random_solution_per_signup(libraries,book_scores,Days) for _ in range(population_size)]
        best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries,0)
        total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Genetic Algorithm: ", total_score, " Time: ", end_time)

        # Genetic Algorithm
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("c_incunabula.txt")
        # Define the parameters for the genetic algorithm
        num_generations = 100  # Number of generations
        population_size = 50  # Size of population
        tournament_size = 20  # Size of tournament for tournament selection
        mutation_rate = 0.1  # Probability of mutation
        ## Create an initial population of random solutions
        population = [utils.random_solution_per_signup(libraries,book_scores,Days) for _ in range(population_size)]
        best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries,0)
        total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Genetic Algorithm: ", total_score, " Time: ", end_time)

        # Genetic Algorithm
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("d_tough_choices.txt")
        # Define the parameters for the genetic algorithm
        num_generations = 100  # Number of generations
        population_size = 50  # Size of population
        tournament_size = 20  # Size of tournament for tournament selection
        mutation_rate = 0.1  # Probability of mutation
        ## Create an initial population of random solutions
        population = [utils.random_solution_per_signup(libraries,book_scores,Days) for _ in range(population_size)]
        best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries,0)
        total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Genetic Algorithm: ", total_score, " Time: ", end_time)

        # Genetic Algorithm
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("e_so_many_books.txt")
        # Define the parameters for the genetic algorithm
        num_generations = 100  # Number of generations
        population_size = 50  # Size of population
        tournament_size = 20  # Size of tournament for tournament selection
        mutation_rate = 0.1  # Probability of mutation
        ## Create an initial population of random solutions
        population = [utils.random_solution_per_signup(libraries,book_scores,Days) for _ in range(population_size)]
        best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries,0)
        total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Genetic Algorithm: ", total_score, " Time: ", end_time)

        # Genetic Algorithm
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("f_libraries_of_the_world.txt")
        # Define the parameters for the genetic algorithm
        num_generations = 100  # Number of generations
        population_size = 50  # Size of population
        tournament_size = 20  # Size of tournament for tournament selection
        mutation_rate = 0.1  # Probability of mutation
        ## Create an initial population of random solutions
        population = [utils.random_solution_per_signup(libraries,book_scores,Days) for _ in range(population_size)]
        best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries,0)
        total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Genetic Algorithm: ", total_score, " Time: ", end_time)

        #Ant Colony Optimization
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("a_example.txt")
        num_iterations = 100
        num_ants = 20
        evaporation_rate = 0.1
        initial_pheromone = 1.0
        alpha = 1  # Pheromone importance
        beta = 2   # Heuristic importance
        initial_random_solution = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_ant_colony = ac.ant_colony_optimization(libraries,book_scores,Days,num_iterations,num_ants,evaporation_rate,initial_pheromone,alpha,beta)
        total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Ant Colony Optimization: ", total_score, " Time: ", end_time)

        #Ant Colony Optimization
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("b_read_on.txt")
        num_iterations = 100
        num_ants = 20
        evaporation_rate = 0.1
        initial_pheromone = 1.0
        alpha = 1  # Pheromone importance
        beta = 2   # Heuristic importance
        initial_random_solution = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_ant_colony = ac.ant_colony_optimization(libraries,book_scores,Days,num_iterations,num_ants,evaporation_rate,initial_pheromone,alpha,beta)
        total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Ant Colony Optimization: ", total_score, " Time: ", end_time)

        #Ant Colony Optimization
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("c_incunabula.txt")
        num_iterations = 100
        num_ants = 20
        evaporation_rate = 0.1
        initial_pheromone = 1.0
        alpha = 1  # Pheromone importance
        beta = 2   # Heuristic importance
        initial_random_solution = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_ant_colony = ac.ant_colony_optimization(libraries,book_scores,Days,num_iterations,num_ants,evaporation_rate,initial_pheromone,alpha,beta)
        total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Ant Colony Optimization: ", total_score, " Time: ", end_time)

        #Ant Colony Optimization
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("d_tough_choices.txt")
        num_iterations = 100
        num_ants = 20
        evaporation_rate = 0.1
        initial_pheromone = 1.0
        alpha = 1  # Pheromone importance
        beta = 2   # Heuristic importance
        initial_random_solution = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_ant_colony = ac.ant_colony_optimization(libraries,book_scores,Days,num_iterations,num_ants,evaporation_rate,initial_pheromone,alpha,beta)
        total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Ant Colony Optimization: ", total_score, " Time: ", end_time)

        #Ant Colony Optimization
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("e_so_many_books.txt")
        num_iterations = 100
        num_ants = 20
        evaporation_rate = 0.1
        initial_pheromone = 1.0
        alpha = 1  # Pheromone importance
        beta = 2   # Heuristic importance
        initial_random_solution = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_ant_colony = ac.ant_colony_optimization(libraries,book_scores,Days,num_iterations,num_ants,evaporation_rate,initial_pheromone,alpha,beta)
        total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Ant Colony Optimization: ", total_score, " Time: ", end_time)

        #Ant Colony Optimization
        start_time = time.time()
        libraries,book_scores,Days = utils.readFile("f_libraries_of_the_world.txt")
        num_iterations = 100
        num_ants = 20
        evaporation_rate = 0.1
        initial_pheromone = 1.0
        alpha = 1  # Pheromone importance
        beta = 2   # Heuristic importance
        initial_random_solution = utils.random_solution_per_signup(libraries,book_scores,Days)
        best_solution_from_ant_colony = ac.ant_colony_optimization(libraries,book_scores,Days,num_iterations,num_ants,evaporation_rate,initial_pheromone,alpha,beta)
        total_score = utils.get_values_from_dict(best_solution_from_ant_colony.books_explored,book_scores)
        end_time = time.time() - start_time
        print("Ant Colony Optimization: ", total_score, " Time: ", end_time)




        # # Genetic Algorithm
        # libraries,book_scores,Days = utils.readFile("a_example.txt")
        # # Define the parameters for the genetic algorithm
        # num_generations = 100  # Number of generations
        # population_size = 50  # Size of population
        # tournament_size = 20  # Size of tournament for tournament selection
        # mutation_rate = 0.1  # Probability of mutation
        # ## Create an initial population of random solutions
        # population = [utils.random_solution(libraries,book_scores,Days) for _ in range(population_size)]
        # initial_solution_random = utils.random_solution(libraries,book_scores,Days)
        # best_solution_from_genetic_algorithm = ga.genetic_algorithm(population,Days,num_generations,tournament_size,mutation_rate,libraries)
        # total_score = utils.get_values_from_dict(best_solution_from_genetic_algorithm.books_explored,book_scores)
        # print("Genetic Algorithm: ", total_score)

    except ValueError as e:
        print(e)
        print("Restarting...")
        main() 





main()








