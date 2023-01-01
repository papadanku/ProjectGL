
"""
Renders a basic scene with a rotating cube
"""

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.sphereGeometry import SphereGeometry

from material.material import Material

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800.0/600.0)
        self.camera.setPosition([0.0, 0.0, 7.0])

        # Initialize sphere object with a radius of 3
        geometry = SphereGeometry(radius=3)

        vertexShader = """
        in vec3 vertexPosition;
        out vec3 position;

        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;

        void main()
        {
            vec4 pos = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
            position = vertexPosition;
        }
        """

        fragmentShader = """
        in vec3 position;
        out vec4 fragColor;

        void main()
        {
            vec3 color = fract(position);
            fragColor = vec4(color, 1.0);
        }
        """

        material = Material(vertexShader, fragmentShader)
        material.locateUniforms()

        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.renderer.render(self.scene, self.camera)

# Instantiate this class and run the program
Test(screenSize=[800,600]).run()
