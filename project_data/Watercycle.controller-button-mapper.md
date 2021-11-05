# ControllerButtonMapper

The purpose of this project is to effectively navigate the desktop and games 
using a gamepad (xbox 360, xbox one, logitech, dualshock, ...).

XMapper and Joy2Key are similar programs, but XMapper costs money (Hurray for 
being cheap!) and Joy2Key does not allow you to directly map your analog stick
input to the mouse for natural movements.  Not to mention that it is a pretty
confusing program in the first place!

# Tested Controllers:
- Xbox One

# Current Features:

- Bind any combination of controller buttons to a keyboard or mouse action.
- Use your Analog Stick as a mouse.
- A simple binding language.
- Mapping Setup

# Todo

- Test more controllers
- ~~Add options to disable bindings and/or mouse input for certain applications~~
  'default.bind' will be used unless a binding is defined for each specific executable.
- Windows only right now but should be easy to extend

# Binding Language Example (with syntax highlighting)

![bindingsyntax](https://cloud.githubusercontent.com/assets/5145006/12012837/2a7c36f8-accd-11e5-80ed-a85198030396.png "Simple Binding Syntax")

(The Notepad++ language theme is included in the settings folder)

You might be wondering why L1 and R1 are red.  That's because they're user defined.  Controllers have mostly the same buttons,
but there are a few unique ones.  So, there is a 'mapping' file that allows people to associate a name with the controller button's
id which is represented as a number from 0 - 31.  Soon enough an option will be added to help setup the controller mappings for 
controllers that do not already have a mapping (like the xbox-one file).

# Dependencies

I am not fully aware of the Windows and Linux API calls necessary and how compatible each of them are.  So, to save a little time, this project uses SFML's JoyStick API, and thus SFML will need to be compiled as well.  The temporarily included version is a Windows 10 64-bit distribution.  Ideally the SFML dependency will be dropped in the future.

# Building

This will only compile on MSVC right now.  The enum library (enum.h) for this program needs some compatibility work since it turns out GCC is a little stricter than expected.
