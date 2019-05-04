import bpy
from random import randint

bpy.ops.object.select_all(action="SELECT")
bpy.ops.opbject.delete(use_global=False)

bpy.ops.object.camera_add(location=(0,0,0))
bpy.ops.object.light_add(type="SUN", view_align=False, location=(0,0,0))


for i in range(0, 100):
    x = randint(-5, 5)
    y = randint(-5, 5)
    z = randint(-5, 5)
    bpy.ops.mesh.primitive_monkey_add(location = (x,y,x))

    bpy.ops.object.modifier_add(type="SUBSURF")
    bpy.context.object.modifiers["Subdivision"].render_levels = 3
    bpy.context.object.modfiers["Subdivision"].levels = 3
    bpy.ops.object.shade_smooth()
