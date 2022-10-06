import os

names = ['cool']

for name in names:
    os.system(f"\"C:\Program Files\Blender Foundation\Blender 3.3\\blender.exe\" --background --python scenes/export-scene.py -- scenes/{name}.blend dist/{name}.scene")
    os.system(f"\"C:\Program Files\Blender Foundation\Blender 3.3\\blender.exe\" --background --python scenes/export-meshes.py -- scenes/{name}.blend dist/{name}.pnct")
    os.system(f"\"C:\Program Files\Blender Foundation\Blender 3.3\\blender.exe\" --background --python scenes/export-walkmeshes.py -- scenes/{name}.blend WalkMesh dist/{name}.w")
