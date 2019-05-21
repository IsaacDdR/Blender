import Blender
from Blender import *
fromo Blender.Scene import Render 

scn = Blender.Scene.Get("Scene")
context. scn.getRenderingContext()

context.extensions = True
context.renderPath = "home/neo"
context.sizePreset = (Render.PAL)
context.imageType = Render.TARGA
context.fps = 25
context.sFrame = 1
context.eFrame = 100

context.renderAnim()


