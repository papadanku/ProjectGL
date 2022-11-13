
from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

# Render two shapes 
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### Initialize program ###
        vertexShader = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.xyz, 1.0);
        }
        """

        fragmentShader = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.programReference = OpenGLUtils.initializeProgram(vertexShader, fragmentShader)

        ### Render settings ###
        glLineWidth(4)

        ### Setup vertex array object - triangle

        # NOTE: Generate 1 vertex array and assign it to triangleVAO
        self.triangleVAO = glGenVertexArrays(1)
        
        # Activate the triangleVAO vertex array
        glBindVertexArray(self.triangleVAO)

        trianglePositionData = [
            [-0.5, 0.8, 0.0],
            [-0.2, 0.2, 0.0],
            [-0.8, 0.2, 0.0]
        ]
        self.triangleVertexCount = len(trianglePositionData)
        trianglePositionAttribute = Attribute("vec3", trianglePositionData)
        trianglePositionAttribute.associateVariable(self.programReference, "position")

        ### Setup vertex array object - square ###
        self.squareVAO = glGenVertexArrays(1)
        glBindVertexArray(self.squareVAO)
        squareDataPosition = [
            [0.8, 0.8, 0.0],
            [0.8, 0.2, 0.0],
            [0.2, 0.2, 0.0],
            [0.2, 0.8, 0.0]
        ]
        self.squareVertexCount = len(squareDataPosition)
        squarePositionAttribute = Attribute("vec3", squareDataPosition)
        squarePositionAttribute.associateVariable(self.programReference, "position")

    def update(self):
        # Using the same program to render both shapes
        glUseProgram(self.programReference)

        # Draw shapes
        # 1. Activate VAO
        # 2. Issue draw-call on the activated vertex array

        # Draw the triangle
        glBindVertexArray(self.triangleVAO)
        glDrawArrays(GL_LINE_LOOP, 0, self.triangleVertexCount)

        # Draw the square
        glBindVertexArray(self.squareVAO)
        glDrawArrays(GL_LINE_LOOP, 0, self.squareVertexCount)

# Instantiate this class and run the program
Test().run()
