## TeachCraft - Globalhack Youth Mini-hackathon

A mini-hackathon challenge for students to build something awesome with code in minecraft!

The shared multi-player server is located here:
```
199.96.85.3:25570
```

You can also setup your own server (if your computer has the resources) following the optional instructions below.

### Setup

[Setup Client](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/setup.md): Get minecraft running, get connected to the server.

[Optional - setup your own server](https://github.com/teachthenet/TeachCraft-Server): If you don't want to use our shared multiplayer server, you can setup your own following these instructions.

### Other neat, complex examples

[Import Images](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/example-import-image/script.py): Learn how to import an image into minecraft pixel art using Python Imaging Library.

[Import 3D Model](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/example-import-3d-image/script.py): Learn how to import a 3d model (such as those used with 3d printers) into Minecraft!

[Build a mini-game: Lavatrap](http://www.stuffaboutcode.com/2015/09/minecraft-game-tutorial-lavatrap-pycon.html) [Link 2](https://docs.google.com/document/d/19YVesJJFS6cg4Ndep7F-TS02CpS0qpN1hlSlv6mgISQ/edit) [Solution](https://github.com/martinohanlon/minecraft-lavatrap/blob/master/lavatrap.py)

[Build An Moving Clock](https://github.com/martinohanlon/minecraft-clock/blob/master/minecraft-clock.py)

[Star Wars Animated](https://github.com/martinohanlon/minecraft-starwars)

[Auto-bridge](http://www.stuffaboutcode.com/2013/02/raspberry-pi-minecraft-auto-bridge.html) [Link 2](https://github.com/martinohanlon/minecraft-bridge)

### Minecraft Docs
- [pi version](http://www.stuffaboutcode.com/p/minecraft-api-reference.html) Has most of the basics of the python api
- [our version](https://github.com/zhuowei/RaspberryJuice) Has the additional things our python api supports, above and beyond the pi version
- [Minecraft block ids](http://minecraft-ids.grahamedgecombe.com/)

### Notes
- Player location from the python api will not match the same retrieved from the server.
    This is because raspberryjuice calculates it from the spawn point, while the server calculates it from 0,0,0.
    To fix, run this as an admin:
    setworldspawn 0 0 0

