
from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

# Render shapes with vertex colors
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### Initialize program ###
        vertexShader = """
        in vec3 position;
        in vec3 vertexColor;
        out vec3 color;
        void main()
        {
            gl_Position = vec4(position.xyz, 1.0);
            color = vertexColor;
        }
        """

        fragmentShader = """
        in vec3 color;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(color.rgb, 1.0);
        }
        """

        self.programReference = OpenGLUtils.initializeProgram(vertexShader, fragmentShader)

        ### Render settings (optional) ###
        glPointSize(10)
        glLineWidth(4)

        ### Setup vertex array object ###
        vaoReference = glGenVertexArrays(1)
        glBindVertexArray(vaoReference)

        ### Setup vertex attributes ###
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
        positionAttribute.associateVariable(self.programReference, "vertexColor")

    def update(self):
        glUseProgram(self.programReference)
        glDrawArrays(GL_POINTS, 0, self.vertexCount)

# Instantiate this class and run the program
Test().run()