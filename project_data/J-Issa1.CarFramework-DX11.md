# DirectX 11 Racing Game Framework

A Engine Framework displaying the basics behind a car racing game.

Included in the project are:

* Player controlled car.
* AI controlled car.
* Different forces which can be applied to objects (gravity, sliding force, drag, acceleration).
* Bounding Sphere Collision.

# Controls

1. WASD - Move
2. Left Shift – Up Gear
3. Left CTRL – Down Gear

# The Player

The player is able to control the main car and they are able to move around the track freely. In order to represent a similar notion to real-life car, I have included a basic gearing system. Also included on the player is collision. This allows for the player to collide with the cubes placed in the world.

The player can move forwards using a constant velocity or a constant accleration speed. This is done via the 1st and 2nd Laws of Motion.

* S = UT + 0.5AT^2
* V = U + AT

This is done through the use a Particle Model (detailed below).

# ParticleModel

The use of a particle model is to give the user the ability to add particles into the system, using the methods given. Included are:

* Basic Movement
* Constant Acceleration
* Constant Velocity
* Forces such as; sliding force, motion in fluid, drag (laminar and turbulent), gravity, mass.

There is the functionality to change the gravity or the mass through the use of inheritance. The car is a derived class of particle model with further functionality called CarParticleModel.

# CarParticleModel

The CarParticleModel class extends from the ParticleModel class by adding on features that a car in real-life has including:

* RPM
* Steering angle
* Engine Speed
* Gear Ration
* Friction Coefficient
* Thrust
* Wheel radius

All of these factors allow for a more lifelike simulation of the system.

# AI

In order to differentiate the AI car from the player, I decided to make the AI a blue car compared to the player's orange. The Ai car moves around the track via waypoints, which can be edited in a seperate txt file. This file is titled 'waypoints.txt'.

Inside the txt file, a new waypoint is signified on a new line starting with a 'w'. This is for the file parser to understand what information is being read in. Waypoints can be edited by changing the numbers. Waypoints are laid out in an 'x, y, z' coordinate system, and are seperated by a space.

I.e. w 51.1540947 0.8 -36.5976219

The AI also calculates the rotation to the next waypoint through the use of an arctangent funtion, by getting the vector between its current waypoint and its position. Then it sets the rotation to be the new angle. 

# Cubes and Collision

Cubes are included to show off the collision and physics system included in the project. When dropped from any distance on the y axis, the cubes bounce and lose height, mirroring real-life bounce. This is due to gravity acting on the cubes. In this project, gravity is presumed to be -9.81.

Also included on the cubes are sliding force which can be toggled on and off through the use of a boolean. The degree at which the sliding force is applied can be changed by the use of the 'SlidingForce' method. 

For Example: 

* Currently when the cubes hit the ground there is a sliding force of 90 degrees applied, meaning they slide horizontally across the ground. 

* However, that were to be 45 degrees, they would fall as if they were sliding down a ramp (or something to that effect). 

# Shader

Also included is a basic shader which takes into account the use of diffuse, ambient and specular lighting. It also oks at specular power and light reflection, as well as texuring and camera 'eye' position. 

Texturing has a basic diffuse texture and linear sampler state.