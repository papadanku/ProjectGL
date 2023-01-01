
"""
Renders a basic scene with a geometry that has 3 triangles
"""

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.geometry import Geometry

from material.surfaceMaterial import SurfaceMaterial

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800.0/600.0)
        self.camera.setPosition([0.0, 0.0, 1.0])

        # Initialize basic 2D geometry object (Z=0)
        geometry = Geometry()

        # Setup geometry's vertex positions for 3 triangles
        P0 = [-0.1,  0.1, 0.0]
        P1 = [ 0.0,  0.0, 0.0]
        P2 = [ 0.1,  0.1, 0.0]
        P3 = [-0.2, -0.2, 0.0]
        P4 = [ 0.2, -0.2, 0.0]
        positionData = [
            P0, P3, P1,
            P1, P3, P4,
            P1, P4, P2,
        ]
        geometry.addAttribute("vec3", "vertexPosition", positionData)

        # Setup geometry's vertex colors for 3 triangles
        R = [1.0, 0.0, 0.0]
        Y = [1.0, 1.0, 0.0]
        G = [0.0, 0.25, 0.0]
        colorData = [
            R, G, Y,
            Y, G, G,
            Y, G, R,
        ]
        geometry.addAttribute("vec3", "vertexColor", colorData)

        # Setup geometry's vertex count
        geometry.countVertices()

        # Setup geometry's material properties
        material = SurfaceMaterial(
            {
                "useVertexColors" : True
            }
        )

        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.renderer.render(self.scene, self.camera)

# Instantiate this class and run the program
Test(screenSize=[800,600]).run()
