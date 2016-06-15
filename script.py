#Show minecraft, show example of running a command in minecraft. Code is similar to running commands in minecraft

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

cobblestone_block_id = 4 
mc.setBlocks(x, y, z, x2, y2, z2, cobblestone_block_id)

#http://minecraft-ids.grahamedgecombe.com/

#How do we make it twice as high? Change y2 value.
mc.setBlocks(x, y, z, x2, y2+5, z2, cobblestone_block_id)

#Change block ID above to something else
mc.setBlocks(x, y, z, x2, y2, z2, 89) #glowstone block ID

#Observe still solid. How to make hollow? Any ideas? (Pull back up ID list)

#What if we made a smaller building out of the block ID for air, inside of the existing building?

air_block_id = 0
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)

#Let's remove the roof, so we can add a custom more complex roof later.
#To do this, let's make a single block tall layer that is pure air, covering the top of the cobblestone building.
#To do this, start y at y2
mc.setBlocks(x, y2, z, x2, y2, z2, air_block_id)

#Fly over it and look down into it after removing the roof.
#"You know, in looking down on it, I kind of want to see how it would look as a swimming pool."
#Let's change the block of the main building into glass, and the inner building into water.
mc.setBlocks(x, y, z, x2, y2, z2, 20) #20 = glass
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, 8) #8 = water
mc.setBlocks(x, y2, z, x2, y2, z2, air_block_id)

#Look how rapidly that changed.
#Let's go back to the mossy cobblestone look though.
mc.setBlocks(x, y, z, x2, y2, z2, cobblestone_block_id)

#And let's add a roof. It will be three layers of wood, in a pyramid shape.
mc.setBlocks(x, y2, z, x2, y2, z2, 5) #5 = wood
mc.setBlocks(x+1, y2+1, z, x2-1, y2+1, z2, 5) #5 = wood
mc.setBlocks(x+2, y2+2, z, x2-2, y2+2, z2, 5) #5 = wood

#You get the picture.

#Another trick you can do is use your character to dictate where things are built.
#Using a while loop, you can cause things to follow behind you

import time 
while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 38)
    time.sleep(0.2) 

#And observe, there's a path of flowers following behind me. You could easily replace this with TNT, or minecraft's railway track to make a roller coaster, for example.

#Other ideas: Maze (with traps?), something moving, large buildings with trap doors activated by code, pixel art, etc

#The challenge is that you must do it in survival mode. This is to encourage you to use code to build things.

#You may want to build a few utility tools first, such as a way to get an aerial view. Consider taking your current position, and creating a block 50 units above you, then using the setPos function to teleport your player on top of that block to look down (for example). Also consider how to defend yourself at night - perhaps you need some offensive or defensive code to protect yourself against the zombies (or sleep the night away, or accept death and just re-teleport yourself to your building location).

#You may also want to record the x/y/z coordinates of the place you are building things at, so if you die you can teleport yourself back there easily.

#Here are the main two links you need to stay on top of
#minecraft functions available: http://www.stuffaboutcode.com/p/minecraft-api-reference.html
#minecraft block ids: http://minecraft-ids.grahamedgecombe.com/

#Respect each other, and don't grief.