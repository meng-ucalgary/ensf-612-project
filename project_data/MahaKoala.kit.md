# The Kit Framework

## WARNING

This is a very shabby upload of my personal one-man project. It is not by any means complete. I have spent 1.5 years working on this in my sparetime. A lot of things will be very dirty, some things will be missing, and some things will seem to exist for no reason at all. This is NOT a cleaned up project. (yet!)

It should be added that a lot in this readme is just plain wrong as well. Check http://svkonsult.se/kit for more information about this project and its uses.

Sharing this mainly for educational reasons, dont expect it to hold any "public release" quality. Enjoy!


## Welcome

### Dependencies

Kit depends on the following libraries:

* GLFW3 (Window and input management)
* Freetype 2 (Text rendering)
* Chaiscript (Scripting)
* OpenGL (Rendering)

### Build & Install

Regular makefile build.

`make -j 10 && sudo make install`

Tip: Use -j 10 to parallelize the object compilation, which makes it compile much faster.

### C++ Library

The C++ library is the main part of the framework. It provides low-level helper classes for OpenGL 4.5, as well as more higher-level classes for rendering terrains, user interfaces, physically based rendering etc. 

### World editor

The world editor is pretty self-explanatory, it is where level/game-designers will do most of their work. It allows you to design levels in the world, as well as place gameplay-related triggers/entities which is then scripted in Your-Favourite-Editor®. This allows the developer to easily design and implement in-game puzzles, quests or even mini-games. This part of the framework is pretty tied to LoN, and might be separated from the framework in the future. 

### Material editor

The material editor is a small (but important) tool that allows graphics designers to adapt assets with realtime feedback. It supports albedo maps, roughness and metalness maps (with adjustable gamma and input/output levels), emissive maps and normal maps (with adjustable normal strength). It also allows the developer to preview materials on custom meshes and even animated models.

### Asset importer

The asset importer is a tool that allows graphics designers to convert 3D assets into files usable by the Kit framework, in a manner that lets the artist preserve relations (between geometry->materials etc.) and asserts artist-controlled naming of the assets. These files includes; Kit Geometry files, Kit Mesh files, Kit Skeleton files (with animations) and Kit Material files. This part is integrated into the material designer.
