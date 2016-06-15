import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob") 

#My position in the world
pos = mc.player.getPos()

# This position is the bottom front right of our building (at my position)
x = pos.x
y = pos.y
z = pos.z

# This position is the top back left of our building.
# Note that we are defining it in relationship to the x/y/z (bottom right front) of our building
# That is to say, the top back left's x value is the bottom right front's x value + 10.
x2 = x + 10
y2 = y + 5
z2 = z + 8

#Change block ID above to something else
mc.setBlocks(x, y, z, x2, y2, z2, 89) #89 = glowstone block ID

#Make it hollow
air_block_id = 0
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)

#Let's remove the roof, so we can add a custom more complex roof later.
#To do this, let's make a single block tall layer that is pure air, covering the top of the cobblestone building.
#To do this, start y at y2
mc.setBlocks(x, y2, z, x2, y2, z2, air_block_id)

#And let's add a roof. It will be three layers of wood, in a pyramid shape.
mc.setBlocks(x, y2, z, x2, y2, z2, 5) #5 = wood
mc.setBlocks(x+1, y2+1, z, x2-1, y2+1, z2, 5) #5 = wood
mc.setBlocks(x+2, y2+2, z, x2-2, y2+2, z2, 5) #5 = wood
