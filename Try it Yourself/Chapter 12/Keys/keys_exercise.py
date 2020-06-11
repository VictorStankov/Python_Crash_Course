import pygame


screen_0 = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Keys")

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event)
