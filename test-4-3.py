
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
from geometry.boxGeometry import BoxGeometry

from material.surfaceMaterial import SurfaceMaterial

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 4])

        geometry = BoxGeometry()
        material = SurfaceMaterial({
            "useVertexColors" : True
        })
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
    
    def update(self):
        self.renderer.render(self.scene, self.camera)
        
# Instantiate this class and run the program
Test(screenSize=[800,600]).run()
