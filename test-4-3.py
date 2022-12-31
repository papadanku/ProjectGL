
"""
Renders a basic scene with a rotating cube
"""

from math import sin
from numpy import arange

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.geometry import Geometry

from material.pointMaterial import PointMaterial
from material.lineMaterial import LineMaterial

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 4])

        # Initialize basic geometric objects
        geometry = Geometry()

        # Setup geometries' position data
        # NOTE: Both line and point meshses share the same vertex positions
        positionData = list()
        for x in arange(-3.2, 3.2, 0.3):
            positionData.append([x, sin(x), 0.0])
        geometry.addAttribute("vec3", "vertexPosition", positionData)
        geometry.countVertices()

        # Setup geometries' material data
        # NOTE: We use the baseColor uniform instead of the vertexColor attributes
        pointMaterial = PointMaterial(
            {
                "baseColor": [1.0, 1.0, 0.0],
                "pointSize": 10.0
            }
        )

        lineMaterial = LineMaterial(
            {
                "baseColor": [1.0, 0.0, 1.0],
                "lineWidth": 4.0
            }
        )

        pointMesh = Mesh(geometry, pointMaterial)
        lineMesh = Mesh(geometry, lineMaterial)
        self.scene.add(pointMesh)
        self.scene.add(lineMesh)

    
    def update(self):
        self.renderer.render(self.scene, self.camera)
        
# Instantiate this class and run the program
Test(screenSize=[800,600]).run()
