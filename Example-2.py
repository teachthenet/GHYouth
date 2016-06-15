import mcpi.minecraft as minecraft
import time 

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob") 

#Make a trail of flowers (block id=38) constantly follow behind the player
while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 38)
    time.sleep(0.2) 
