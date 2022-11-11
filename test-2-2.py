
"""
Draws a single point on the screen
"""

from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils

# Render a single point
# papadanku: We inherit the Base class and extend its functionality
class Test(Base):

    def initialize(self):

        print("Initializing program...")

        ### Initialize the program ###

        # Vertex shader code
        vertexShader = """
        void main()
        {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """

        # Fragment shader code
        fragmentShader = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        # Send code to the GPU and compile; store the program's reference value
        self.programReference = OpenGLUtils.initializeProgram(vertexShader, fragmentShader)

        ### Set up vertex array object ###
        vaoReference = glGenVertexArrays(1)
        glBindVertexArray(vaoReference)

        ### Render settings (optional) ###

        # Set point's width and height
        glPointSize(10)

    def update(self):

        # Select program to use when rendering
        glUseProgram(self.programReference)

        # Renders geometric objects using selected program
        # papadanku: 1 draw call -_-
        glDrawArrays(GL_POINTS, 0, 1)

# Instantiate this class and run the program
Test().run()