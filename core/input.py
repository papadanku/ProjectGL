
import pygame

class Input(object):

    def __init__(self):
        # Has the user quit the application?
        self.quit = False

        # Lists to store key states
        # Down, up: Discrete event; lasts for one iteration
        # Pressed: Continuous even, between up and down events

        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []

    def update(self):
        """
        Iterate all over user input events (such as keyboard or mouse)
        that occured since the last time events were checked
        """

        # Reset discrete key states
        self.keyDownList = []
        self.keyUpList = []

        for event in pygame.event.get():
            """
            Check for keydown and keyup events;
                get name of key from event
                and append to or remove from corresponding lists
            """
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)

            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)

            # Quit event occurs by clicking button to close window
            if event.type == pygame.quit:
                self.quit = True

    # Functions to check key states in the list
    def isKeyDown(self, keyCode):
        return keyCode in self.keyDownList

    def isKeyPressed(self, keyCode):
        return keyCode in self.keyDownList

    def isKeyUp(self, keyCode):
        return keyCode in self.keyUpList
