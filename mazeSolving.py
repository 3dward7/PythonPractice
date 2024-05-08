import pygame
from random import choice

# Initialization
RES = WIDTH, HEIGHT = 800, 600
TILE = 40
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# Cell class definition
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.solution_step = False  # Marks if the cell is part of the solution path

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('black'), (x, y, TILE, TILE))
        else:
            return
        if self.solution_step:
            pygame.draw.rect(sc, pygame.Color('green'), (x + 2, y + 2, TILE - 4, TILE - 4))

        # Drawing walls
        walls_color = pygame.Color('white')  # Walls color
        if self.walls['top']:
            pygame.draw.line(sc, walls_color, (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pygame.draw.line(sc, walls_color, (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pygame.draw.line(sc, walls_color, (x + TILE, y + TILE), (x, y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(sc, walls_color, (x, y + TILE), (x, y), 2)

    # Other methods remain unchanged from your original script

def remove_walls(a, b):
    # Your original remove_walls function without modification

# Maze generation and maze solving functions
def generate_maze():
    # Initialize maze generation variables
    for cell in grid_cells:
        cell.visited = False
    stack = [grid_cells[0]]

    while stack:
        current = stack[-1]
        current.visited = True
        neighbors = [grid_cells[n] for n in current.check_neighbors()]  # Adjust the check_neighbors to return indexes
        if neighbors:
            next_cell = choice(neighbors)
            remove_walls(current, next_cell)
            stack.append(next_cell)
        else:
            stack.pop()

def solve_maze():
    # Initialize maze solving variables
    for cell in grid_cells:
        cell.solution_step = False
        cell.visited = False

    stack = [grid_cells[0]]

    while stack:
        current = stack[-1]
        current.visited = True
        if current == grid_cells[-1]:  # If it's the exit cell
            for cell in stack:
                cell.solution_step = True
            return

        neighbors = [grid_cells[n] for n in current.check_neighbors() if not grid_cells[n].visited and no_wall_between(current, grid_cells[n])]
        if neighbors:
            next_cell = choice(neighbors)
            stack.append(next_cell)
        else:
            stack.pop()

# Helper function to check if there's no wall between two cells (to be written)

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]  # Initialize grid

def game_loop():
    generate_maze()
    solve_maze()

    while True:
        sc.fill(pygame.Color('darkslategray'))  # Background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw maze
        for cell in grid_cells:
            cell.draw()

        pygame.display.flip()
        clock.tick(30)

game_loop()
pygame.quit()
