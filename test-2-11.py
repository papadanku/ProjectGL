
from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform

# Animate triable moved accross the screen
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### Initialize program ###
        vertexShader = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.xyz, 1.0);
        }
        """

        fragmentShader = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor.rgb, 1.0);
        }
        """

        self.programReference = OpenGLUtils.initializeProgram(vertexShader, fragmentShader)

        ### Render settings (optional) ###

        ### Specify color used when clearing ###
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### Setup Vertex Array Object ###
        vaoReference = glGenVertexArrays(1)
        glBindVertexArray(vaoReference)

        ### Setup vertex attributes ###
        positionData = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programReference, "position")

        ### Setup uniforms ###
        self.translation = Uniform("vec3", [0.0, 0.0, 0.0])
        self.translation.locateVariable(self.programReference, "translation")

        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable(self.programReference, "baseColor")

        # Triangle speed, units per second
        self.speed = 0.5

    def update(self):

        ### Update data ###

        distance = self.speed * self.deltaTime

        if self.input.isKeyPressed("left"):
            self.translation.data[0] -= distance
        if self.input.isKeyPressed("right"):
            self.translation.data[0] += distance
        if self.input.isKeyPressed("down"):
            self.translation.data[1] -= distance
        if self.input.isKeyPressed("up"):
            self.translation.data[1] += distance

        ### Render scene ###

        # Reset the color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.programReference)

        # Upload the updated data to the uniform attribute
        self.translation.uploadData()
        self.baseColor.uploadData()

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# Instantiate this class and run the program
Test().run()