
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

        geometry = SphereGeometry(radius=3, radiusSegments=128, heightSegments=64)

        vertexShader = """
        in vec3 vertexPosition;
        in vec3 vertexColor;
        out vec3 color;

        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        uniform float time;

        void main()
        {
            float offset = 0.2 * sin(8.0 * vertexPosition.x + time);

            // Offset by Y-axis
            vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);

            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1.0);

            color = vertexColor;
        }
        """

        fragmentShader = """
        in vec3 color;
        out vec4 fragColor;
        uniform float time;

        void main()
        {
            float r = abs(sin(time));
            vec4 c = r * vec4(1.0, -0.5, -0.5, 0.0);

            // Composite a sine of red over vertex color
            fragColor = vec4(color, 1.0) + c;
        }
        """

        material = Material(vertexShader, fragmentShader)
        material.addUniform("float", "time", 0)
        material.locateUniforms()

        self.time = 0
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.time += 1/60
        self.mesh.material.uniforms["time"].data = self.time
        self.renderer.render(self.scene, self.camera)

# Instantiate this class and run the program
Test(screenSize=[800,600]).run()
