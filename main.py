from matrix import Matrix

# sizeX=189 # Size Horizontal (Automated)
sizeY=300 # Size Vertical
rf=0.08 # Refresh Per Second

minT=5 # Min Size Tile
maxT=13 # Max Size Tile

minOf=5 # Min Size Offset
maxOf=15 # Max Size Offset

matrix = Matrix(sizeY,rf,minT,maxT,minOf,maxOf)

matrix.Setup()