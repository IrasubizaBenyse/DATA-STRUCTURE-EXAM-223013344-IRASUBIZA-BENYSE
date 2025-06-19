This program simulates how different traffic lights operate using object-oriented programming in C++.
It models the behavior of basic traffic lights and pedestrian signals, allowing them to switch between different colors (or states) based on time durations.
1. State Representation
   
Each light state (like "Red" or "Walk") is stored with:
A color name (like Red, Green, Walk)
A duration (how long that color should stay active)
These light states are stored as an array in each traffic controller.

 How the Program Runs
It creates one basic traffic light and one pedestrian light with their respective color states.
Both are added to the manager.
The manager runs both controllers together in a loop, showing which color is active and for how long.
After a few cycles, the basic light is removed, and only the pedestrian light keeps running.

Example Behavior
Cycle 1:
BasicController: Red for 5 seconds
PedestrianController: Walk for 4 seconds

Cycle 2:
BasicController: Green for 3 seconds
PedestrianController: Don’t Walk for 6 seconds

...

After removing the BasicController:
PedestrianController: Walk for 4 seconds

Controller Manager

This is a special part of the program that manages multiple controllers (basic or pedestrian). It can:
Add new controllers
Remove controllers
Cycle all the traffic lights at once
This means you can simulate many traffic lights running together.

Key Concepts Used in This Program

Object-Oriented Programming: It uses classes, inheritance, and polymorphism to build reusable and organized code.
Dynamic Memory: It creates objects and state arrays in memory at runtime and deletes them when no longer needed.
Polymorphism: Even though the manager only sees the base controller type, it correctly calls the behavior of each specific type (basic or pedestrian).

