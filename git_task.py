import pygame
import random
import time

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

GRID_COLUMNS = 10
GRID_ROWS = 10

CELL_SIZE = WINDOW_WIDTH // GRID_COLUMNS

REFRESH_INTERVAL_SECONDS = 5

BACKGROUND_COLOR = (0, 0, 0)


WINDOW_TITLE = "Procedural Color Grid (Auto-Refresh: 5s)"


def generate_color_grid():
    """
    Genereaza o matrice 10x10 de culori RGB aleatoare.

    Fiecare celula din matrice contine un tuplu (R, G, B) cu valori
    aleatoare in intervalul [0, 255].

    Returneaza:
        list[list[tuple]]: Matricea de culori generata
    """
    color_grid = []

    for row in range(GRID_ROWS):
        color_row = []

        for col in range(GRID_COLUMNS):
            random_red   = random.randint(0, 255)
            random_green = random.randint(0, 255)
            random_blue  = random.randint(0, 255)

            random_color = (random_red, random_green, random_blue)
            color_row.append(random_color)

        color_grid.append(color_row)

    return color_grid


def draw_color_grid(screen, color_grid):
    """
    Deseneaza grila de culori pe fereastra pygame.

    Fiecare celula din matricea de culori este desenata ca un patrat
    de dimensiune CELL_SIZE x CELL_SIZE pixeli.

    Parametri:
        screen (pygame.Surface): Suprafata pe care se deseneaza
        color_grid (list[list[tuple]]): Matricea de culori de desenat
    """
    for row_index in range(GRID_ROWS):
        for col_index in range(GRID_COLUMNS):

            cell_color = color_grid[row_index][col_index]

            cell_x = col_index * CELL_SIZE
            cell_y = row_index * CELL_SIZE

            cell_rect = (cell_x, cell_y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, cell_color, cell_rect)


def main():
    """
    Functia principala a programului.

    Initializeaza pygame, creeaza fereastra si ruleaza bucla principala
    care deseneaza grila si o regenereaza automat la fiecare
    REFRESH_INTERVAL_SECONDS secunde.
    """
    pygame.init()


    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

   
    color_grid = generate_color_grid()

   
    last_refresh_time = time.time()

    is_running = True

    while is_running:

        
        current_time = time.time()
        elapsed_time = current_time - last_refresh_time

        if elapsed_time >= REFRESH_INTERVAL_SECONDS:
            color_grid = generate_color_grid()
            last_refresh_time = current_time

     
        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                color_grid = generate_color_grid()
                last_refresh_time = time.time()

       
        screen.fill(BACKGROUND_COLOR)

        draw_color_grid(screen, color_grid)


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
