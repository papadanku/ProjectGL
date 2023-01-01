
from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

# Render six points in a hexagon arrangement
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### Initialize program ###

        # Vertex shader code
        # NOTE: "position" is our vertex attribute
        vertexShader = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.xyz, 1.0);
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

        ### Setup vertex array object ###

        # Generate and bind 1 vertex array object
        vaoReference = glGenVertexArrays(1)
        glBindVertexArray(vaoReference)

        ### Render settings (optional) ###
        glLineWidth(10)

        ### Setup vertex attribute ###
        positionData = [
            [0.8, 0.0, 0.0],
            [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],
            [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],
            [0.4, -0.6, 0.0]
        ]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programReference, "position")

    def update(self):

        # Select program to use when rendering
        glUseProgram(self.programReference)

        # Renders geometric objects using selected program
        # NOTE: 1 draw call -_-
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)

# Instantiate this class and run the program
Test().run()