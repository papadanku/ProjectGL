
from core.base import Base

# Check input
class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):

        """
        # Debug printing
        if len(self.input.keyDownList) > 0:
            print("Keys down:", self.input.keyDownList)

        if len(self.input.keyPressedList) > 0:
            print("Keys pressed:", self.input.keyPressedList)

        if len(self.input.keyUpList) > 0:
            print("Keys up:", self.input.keyUpList)
        """

        # Typical usage
        if self.input.isKeyDown("space"):
            print("The 'space' key was just pressed down.")
        
        if self.input.isKeyPressed("right"):
            print("The 'right' key is currently being pressed.")

# Instantiate this class and run the program
Test().run()
