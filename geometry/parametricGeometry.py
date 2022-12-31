
"""
Extends the Geometry class to generate parametric geometry
"""

from geometry.geometry import Geometry

class ParametricGeometry(Geometry):

    def __init__(self, uStart, uEnd, uResolution, vStart, vEnd, vResolution, surfaceFunction):

        # Generate a set of points on function
        deltaU = (uEnd - uStart) / uResolution
        deltaV = (vEnd - vStart) / vResolution
        positions = list()

        # Generate local vertex positions based on given deltas and surface function
        for uIndex in range(uResolution+1):
            vArray = list()
            for vIndex in range(vResolution+1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                vArray.append(surfaceFunction(u,v))
                positions.append(vArray)

        # Store vertex data
        positionData = list()
        colorData = list()

        # Default vertex colors
        C1, C2, C3 = [1,0,0], [0,1,0], [0,0,1]
        C4, C5, C6 = [0,1,1], [1,0,1], [1,1,0]

        # Group local vertex position data into triangles
        # NOTE: .copy() is necessary to avoid storing references
        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                # Position data
                pA = positions[xIndex+0][yIndex+0]
                pB = positions[xIndex+1][yIndex+0]
                pD = positions[xIndex+0][yIndex+1]
                pC = positions[xIndex+1][yIndex+1]
                positionData += [
                    pA.copy(), pB.copy(), pC.copy(),
                    pA.copy(), pC.copy(), pD.copy()
                ]

                # Color data
                colorData += [C1,C2,C3, C4,C5,C6]

        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()
