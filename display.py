import pygame
import sys
import main
import utils
import hill_climbing
import simulated_annealing
import tabu_search
import genetic_algorithm

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define font
font = pygame.font.Font(None, 36)

# Define menu options
options = ["Run Optimization Problem", "Quit"]

# Define algorithm options
algorithms = ["Hill Climbing", "Simulated Annealing", "Tabu Search", "Genetic Algorithm"]

# Define a flag to indicate whether the submenu should be drawn
draw_submenu = False

# Define initial solution options
initial_solutions = ["Random", "Greedy"]

files = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices", "e_so_many_books", "f_libraries_in_the_world"]

# Define a flag to indicate whether the initial solution submenu should be drawn
draw_initial_solution_submenu = False

selected_algorithm = None
selected_initial_solution = None
selected_file = None
running_optimization = False


def display_current_state(current_state_value):
    # Clear the screen
    screen.fill(BLACK)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Render the current state value
    text = font.render(f"Current State Value: {current_state_value}", True, WHITE)

    # Display the text
    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

def show_score(solution):
    # Clear the screen
    screen.fill(BLACK)

    # Display the total number of libraries explored
    screen.blit(font.render(f"Total Libraries Explored: {len(solution.library_explored)}", True, WHITE), (50, 50))

    # Display each library and its explored books
    # Display each library and its explored books
    y_offset = 100
    for library in solution.library_explored:
        # Display the library id and the number of books explored
        screen.blit(font.render(f"Library {library.id} - Books Explored: {len(solution.books_explored[library.id])}", True, WHITE), (50, y_offset))
        y_offset += 50

        # Display the id of each explored book
        book_ids = [str(book_id) for book_id in solution.books_explored[library.id]]
        x_offset = 50
        for book_id in book_ids:
            screen.blit(font.render(book_id, True, WHITE), (x_offset, y_offset))
            x_offset += 50  # Adjust this value to give more or less space between the IDs

        y_offset += 50  # Move to the next line for the next library

    # Show the total score 
    screen.blit(font.render(f"Total Score: {solution.get_value(solution.current_day)[0]}", True, WHITE), (50, y_offset))

    # Update the display
    pygame.display.flip()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
def display_black_screen():
    screen = pygame.display.set_mode((800, 600))  # Set the width and height of the screen (width, height).
    screen.fill((0, 0, 0))  # Fill the screen with black color
    pygame.display.flip()  # Update the screen

def run_optimization_problem(libraries,book_scores,days):
    global running
    global running_optimization
    running_optimization = True
    while running_optimization: 
        screen.fill(BLACK)
        print(running_optimization)
        if selected_initial_solution == "Random": 
            initial_solution = utils.random_solution(libraries, book_scores, days)

        solution = None
        while solution is None:
            print("Running Hill Climbing")
            if selected_algorithm == "Hill Climbing":
                solution = hill_climbing.hill_climbing_first_accept(initial_solution,days,libraries)
            elif selected_algorithm == "Simulated Annealing":
                solution = simulated_annealing.simulated_annealing(initial_solution,days,libraries)
            
        running_optimization = False
        show_score(solution)



def choose_file():
    global draw_file_submenu
    draw_file_submenu = True
    global selected_file
    global running 
    while draw_file_submenu:
        # Clear the screen
        screen.fill(BLACK)

        # Display the file options
        for i, text in enumerate(files):
            pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50 + i * 60, 200, 50))
            screen.blit(font.render(text, True, BLACK), (60, 60 + i * 60))

        # Update the display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, rect in enumerate([pygame.Rect(50, 50 + i * 60, 200, 50) for i in range(len(files))]):
                    if rect.collidepoint(x, y):
                        print(f"You selected {files[i]}")
                        selected_file = files[i]
                        draw_file_submenu = False
                        libraries, book_scores, days =  utils.readFile(selected_file)
                        run_optimization_problem(libraries,book_scores,days)
                        return

def choose_initial_solution():
    global draw_initial_solution_submenu
    draw_initial_solution_submenu = True
    global selected_initial_solution
    global running 
    while draw_initial_solution_submenu:
        # Clear the screen
        screen.fill(BLACK)

        # Display the initial solution options
        for i, text in enumerate(initial_solutions):
            pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50 + i * 60, 200, 50))
            screen.blit(font.render(text, True, BLACK), (60, 60 + i * 60))

        # Update the display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, rect in enumerate([pygame.Rect(50, 50 + i * 60, 200, 50) for i in range(len(initial_solutions))]):
                    if rect.collidepoint(x, y):
                        print(f"You selected {initial_solutions[i]}")
                        selected_initial_solution = initial_solutions[i]
                        draw_initial_solution_submenu = False
                        choose_file()
                        return

def choose_algorithm():
    global draw_submenu
    global selected_algorithm
    draw_submenu = True
    global running 

    while draw_submenu:
        # Clear the screen
        screen.fill(BLACK)

        # Display the algorithm options
        for i, text in enumerate(algorithms):
            pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50 + i * 60, 200, 50))
            screen.blit(font.render(text, True, BLACK), (60, 60 + i * 60))

        # Update the display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, rect in enumerate([pygame.Rect(50, 50 + i * 60, 200, 50) for i in range(len(algorithms))]):
                    if rect.collidepoint(x, y):
                        print(f"You selected {algorithms[i]}")
                        selected_algorithm = algorithms[i]
                        draw_submenu = False
                        choose_initial_solution()
                        return

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Check if a key has been pressed
            if event.key == pygame.K_q:  # Check if the key is 'q'
                running = False  # Exit the program
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if not draw_submenu:
                for i, rect in enumerate([pygame.Rect(50, 50 + i * 60, 200, 50) for i in range(len(options))]):
                    if rect.collidepoint(x, y):
                        if options[i] == "Run Optimization Problem":
                            choose_algorithm()
                        elif options[i] == "Quit":
                            running = False

    # Clear the screen
    screen.fill(BLACK)

    if draw_submenu:
        for i, text in enumerate(algorithms):
            pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50 + i * 60, 200, 50))
            screen.blit(font.render(text, True, BLACK), (60, 60 + i * 60))
    else:
        for i, text in enumerate(options):
            pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50 + i * 60, 200, 50))
            screen.blit(font.render(text, True, BLACK), (60, 60 + i * 60))

    # Update the display
    pygame.display.flip()


