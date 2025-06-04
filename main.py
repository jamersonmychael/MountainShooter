import sys

import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup End")

print("Loop Start")
while True:
    #Check for all events // Checa todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close Widow // Fecha Janela
            quit() # End pygame // Fim do pygame

