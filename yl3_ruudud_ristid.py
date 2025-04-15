import pygame

# Funktsioon ruudustiku joonistamiseks
def draw_grid(screen, square_size, rows, cols, line_color):
    screen.fill((144, 238, 144))  # Hele roheline taust
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, line_color, rect, 1)  # Joone paksus 1 px

# Põhifunktsioon mängu käivitamiseks
def run_game(square_size, rows, cols, line_color):
    pygame.init()

    width, height = 640, 480  # Ekraani suurus
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Harjutamine")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(screen, square_size, rows, cols, line_color)
        pygame.display.flip()

    pygame.quit()

# Kasutajalt sisendi küsimine
def get_user_input():
    square_size = int(input("Sisesta ruudu suurus pikslites: "))
    rows = int(input("Sisesta ridade arv: "))
    cols = int(input("Sisesta veergude arv: "))

    print("Sisesta joone värv (R, G, B) kujul (0-255):")
    r = int(input("Punane (R): "))
    g = int(input("Roheline (G): "))
    b = int(input("Sinine (B): "))

    return square_size, rows, cols, (r, g, b)

# Mängu käivitamine kasutaja määratud parameetritega
if __name__ == "__main__":
    square_size, rows, cols, line_color = get_user_input()
    run_game(square_size, rows, cols, line_color)
