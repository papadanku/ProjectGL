
import pygame

class Input(object):

    def __init__(self):
        # has the user quit the application?
        self.quit = False

    def update(self):
        """
        Iterate all over user input events (such as keyboard or mouse)
        that occured since the last time events were checked
        """
        for event in pygame.event.get():
            # quit event occurs by clicking button to close window
            if event.type == pygame.quit:
                self.quit = True
