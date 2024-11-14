# Copyright (c) 2024 Victor Mateevitsi <mvictoras@gmail.com>
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import vtk

def load_texture(filename):
    texture = vtk.vtkTexture()
    image_reader = vtk.vtkJPEGReader()  # Use vtkPNGReader for PNG files
    image_reader.SetFileName(filename)  # Replace with your image path
    texture.SetInputConnection(image_reader.GetOutputPort())

    return texture

def create_glass_sphere(position, radius):
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(position)
    sphereSource.SetRadius(radius)
  
    sphereSource.SetPhiResolution(100)
    sphereSource.SetThetaResolution(100)
    

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())

    actor = vtk.vtkActor()
    actor.GetProperty().SetInterpolationToPBR()
    actor.GetProperty().SetBaseColorTexture(load_texture("Metal049A_1K-JPG_Color/Metal049A_1K-JPG_Color.jpg"))
    actor.GetProperty().SetNormalTexture(load_texture("Metal049A_1K-JPG_Color/Metal049A_1K-JPG_NormalGL.jpg"))
    # This line crashes:
    #actor.GetProperty().SetORMTexture(load_texture("Metal049A_1K-JPG_Color/Metal049A_1K-JPG_orm.jpg"))
    
    actor.GetProperty().SetColor(0.8, 0.8, 0.8)       # White color for clear glass
    actor.GetProperty().SetMetallic(1.0)              # Non-metallic material
    actor.GetProperty().SetRoughness(0.3)            # Low roughness for a shiny surface
    actor.GetProperty().SetMaterialName("physicallyBased")
    actor.SetMapper(mapper)

    return actor

    
# Function to create Cornell Box geometry from vertices and indices
def create_cornell_box(vertices, indices, colors):
    # Setup for VTK poly data structure
    points = vtk.vtkPoints()
    triangles = vtk.vtkCellArray()
    color_array = vtk.vtkUnsignedCharArray()
    color_array.SetNumberOfComponents(3)
    color_array.SetName("Colors")
    
    # Add vertices
    for vertex in vertices:
        points.InsertNextPoint(vertex)
    
    # Add triangles and color data
    for i, face in enumerate(indices):
        triangle = vtk.vtkTriangle()
        triangle.GetPointIds().SetId(0, face[0])
        triangle.GetPointIds().SetId(1, face[1])
        triangle.GetPointIds().SetId(2, face[2])
        triangles.InsertNextCell(triangle)
        
        # Convert float color to unsigned char color for VTK
        color = [int(c * 255) for c in colors[i][:3]]
        color_array.InsertNextTuple(color)
    
    # Set up poly data
    poly_data = vtk.vtkPolyData()
    poly_data.SetPoints(points)
    poly_data.SetPolys(triangles)
    poly_data.GetCellData().SetScalars(color_array)
    
    # Create a mapper and actor for the Cornell Box
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly_data)
    
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    
    return actor

vertices = [
    # Floor
    [1.00, -1.00, -1.00],
    [-1.00, -1.00, -1.00],
    [-1.00, -1.00, 1.00],
    [1.00, -1.00, 1.00],
    # Ceiling
    [1.00, 1.00, -1.00],
    [1.00, 1.00, 1.00],
    [-1.00, 1.00, 1.00],
    [-1.00, 1.00, -1.00],
    # Backwall
    [1.00, -1.00, 1.00],
    [-1.00, -1.00, 1.00],
    [-1.00, 1.00, 1.00],
    [1.00, 1.00, 1.00],
    # RightWall
    [-1.00, -1.00, 1.00],
    [-1.00, -1.00, -1.00],
    [-1.00, 1.00, -1.00],
    [-1.00, 1.00, 1.00],
    # LeftWall
    [1.00, -1.00, -1.00],
    [1.00, -1.00, 1.00],
    [1.00, 1.00, 1.00],
    [1.00, 1.00, -1.00],
    # ShortBox Top Face
    [-0.53, -0.40, -0.75],
    [-0.70, -0.40, -0.17],
    [-0.13, -0.40, -0.00],
    [0.05, -0.40, -0.57],
    # ShortBox Left Face
    [0.05, -1.00, -0.57],
    [0.05, -0.40, -0.57],
    [-0.13, -0.40, -0.00],
    [-0.13, -1.00, -0.00],
    # ShortBox Front Face
    [-0.53, -1.00, -0.75],
    [-0.53, -0.40, -0.75],
    [0.05, -0.40, -0.57],
    [0.05, -1.00, -0.57],
    # ShortBox Right Face
    [-0.70, -1.00, -0.17],
    [-0.70, -0.40, -0.17],
    [-0.53, -0.40, -0.75],
    [-0.53, -1.00, -0.75],
    # ShortBox Back Face
    [-0.13, -1.00, -0.00],
    [-0.13, -0.40, -0.00],
    [-0.70, -0.40, -0.17],
    [-0.70, -1.00, -0.17],
    # ShortBox Bottom Face
    [-0.53, -1.00, -0.75],
    [-0.70, -1.00, -0.17],
    [-0.13, -1.00, -0.00],
    [0.05, -1.00, -0.57],
    # TallBox Top Face
    [0.53, 0.20, -0.09],
    [-0.04, 0.20, 0.09],
    [0.14, 0.20, 0.67],
    [0.71, 0.20, 0.49],
    # TallBox Left Face
    [0.53, -1.00, -0.09],
    [0.53, 0.20, -0.09],
    [0.71, 0.20, 0.49],
    [0.71, -1.00, 0.49],
    # TallBox Front Face
    [0.71, -1.00, 0.49],
    [0.71, 0.20, 0.49],
    [0.14, 0.20, 0.67],
    [0.14, -1.00, 0.67],
    # TallBox Right Face
    [0.14, -1.00, 0.67],
    [0.14, 0.20, 0.67],
    [-0.04, 0.20, 0.09],
    [-0.04, -1.00, 0.09],
    # TallBox Back Face
    [-0.04, -1.00, 0.09],
    [-0.04, 0.20, 0.09],
    [0.53, 0.20, -0.09],
    [0.53, -1.00, -0.09],
    # TallBox Bottom Face
    [0.53, -1.00, -0.09],
    [-0.04, -1.00, 0.09],
    [0.14, -1.00, 0.67],
    [0.71, -1.00, 0.49]
]

indices = [
    [0, 1, 2], [0, 2, 3],         # Floor
    [4, 5, 6], [4, 6, 7],         # Ceiling
    [8, 9, 10], [8, 10, 11],      # Backwall
    [12, 13, 14], [12, 14, 15],   # RightWall
    [16, 17, 18], [16, 18, 19],   # LeftWall
    [20, 22, 23], [20, 21, 22],   # ShortBox Top Face
    [24, 25, 26], [24, 26, 27],   # ShortBox Left Face
    [28, 29, 30], [28, 30, 31],   # ShortBox Front Face
    [32, 33, 34], [32, 34, 35],   # ShortBox Right Face
    [36, 37, 38], [36, 38, 39],   # ShortBox Back Face
    [40, 41, 42], [40, 42, 43],   # ShortBox Bottom Face
    [44, 45, 46], [44, 46, 47],   # TallBox Top Face
    [48, 49, 50], [48, 50, 51],   # TallBox Left Face
    [52, 53, 54], [52, 54, 55],   # TallBox Front Face
    [56, 57, 58], [56, 58, 59],   # TallBox Right Face
    [60, 61, 62], [60, 62, 63],   # TallBox Back Face
    [64, 65, 66], [64, 66, 67]    # TallBox Bottom Face
]

colors = [
    # Floor
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # Ceiling
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # Backwall
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # RightWall
    [0.140, 0.450, 0.091, 1.0], [0.140, 0.450, 0.091, 1.0],
    [0.140, 0.450, 0.091, 1.0], [0.140, 0.450, 0.091, 1.0],
    # LeftWall
    [0.630, 0.065, 0.05, 1.0], [0.630, 0.065, 0.05, 1.0],
    [0.630, 0.065, 0.05, 1.0], [0.630, 0.065, 0.05, 1.0],
    # ShortBox Top Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # ShortBox Left Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # ShortBox Front Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # ShortBox Right Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # ShortBox Back Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # ShortBox Bottom Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # TallBox Top Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # TallBox Left Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # TallBox Front Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # TallBox Right Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # TallBox Back Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    # TallBox Bottom Face
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0],
    [0.725, 0.710, 0.68, 1.0], [0.725, 0.710, 0.68, 1.0]
]

# Create a Cornell Box actor
cornell_box_actor = create_cornell_box(vertices, indices, colors)
glass_sphere = create_glass_sphere([-0.53, -0.1, -0.5], 0.3)

# Set up renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderer.AddActor(cornell_box_actor)
renderer.AddActor(glass_sphere)
renderer.SetBackground(0.3, 0.3, 0.3)

# Create a render pass using vtkAnariPass
anariPass = vtk.vtkAnariPass()
ad = anariPass.GetAnariDevice()
ad.SetupAnariDeviceFromLibrary("environment", "default")
ar = anariPass.GetAnariRenderer()
ar.SetParameter("ambientRadiance", 1.2)
ar.SetParameter("denoiser", True)
ar.SetParameter("denoiseQuality", "high")

# Assign the ANARI render pass to the renderer
renderer.SetPass(anariPass)

vtk.vtkAnariSceneGraph.SetCompositeOnGL(renderer, 1)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(1920, 1920)  # Set render window size
render_interactor = vtk.vtkRenderWindowInteractor()
render_interactor.SetRenderWindow(render_window)

# Configure light source
light = vtk.vtkLight()
light.SetPosition(1, 0, -4)
light.PositionalOn()
light.SetFocalPoint(0, 0, 0)
light.SetIntensity(10)
renderer.AddLight(light)

# Setup the camera to view the front of the Cornell Box
camera = vtk.vtkCamera()
camera.SetPosition(0, 0, -4)        # Set the camera slightly in front of the box
camera.SetFocalPoint(0, 0, 0)      # Look at the center of the box
camera.SetViewUp(0, 1, 0)          # Set the up direction for the camera

renderer.SetActiveCamera(camera)

# Start the rendering process
render_window.Render()
render_interactor.Start()

# Create a window-to-image filter to capture the render
#windowToImageFilter = vtk.vtkWindowToImageFilter()
#windowToImageFilter.SetInput(renderWindow)
#windowToImageFilter.SetScale(1)  # Image quality scaling
#windowToImageFilter.SetInputBufferTypeToRGBA()  # Capture full color buffer
#windowToImageFilter.ReadFrontBufferOff()  # Read from the back buffer
#windowToImageFilter.Update()

# Save the image to a PNG file
#writer = vtk.vtkPNGWriter()
#writer.SetFileName("anari_render.png")
#writer.SetInputConnection(windowToImageFilter.GetOutputPort())
#writer.Write()

#print("Render saved to 'anari_render.png'")