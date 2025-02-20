# Import Statements
import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Print info 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        pygame.display.flip()    

if __name__ == "__main__":
    main()