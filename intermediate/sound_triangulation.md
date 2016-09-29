# Title

Listening for Incoming Aircraft

# Difficulty

Intermediate

# Tags

math, geometry

# Description

You're the operator of a small squadron stationed along the coast listening for incoming enemy aircraft. This is before RADAR, and so your team is equipped with giant microphones and headphones that they use to constantly scour the skies for signs of incoming aircraft. All they are able to get to you is the angle and direction in which they heard a propeller. 

Acoustic location is the science of using sound to determine the distance and direction of something. As a military air defense tool, passive acoustic location was used from mid-World War I to the early years of World War II to detect enemy aircraft by picking up the noise of their engines. Most of the work on anti-aircraft sound ranging was done by the British. They developed an extensive network of sound mirrors that were used from World War I through World War II. Sound mirrors normally work by using moveable microphones to find the angle that maximizes the amplitude of sound received, which is also the bearing angle to the target. Two sound mirrors at different positions will generate two different bearings, which allows the use of triangulation to determine a sound source's position.

Your task today is to be the operator of such a network - given locations of your operators and their reports, can you figure out where are the enemy aircraft? Hurry, you have to scramble the fighters to defend your nation.

# Input Description

You'll be given two reports for one inbound aircraft as a row of three numbers: the first two are the X and Y coordinates of the station as integers, the third is the angle for maximum sound amplitude as a floating point number. This angle will be 0-360, clockwise starting in the top for 0 degrees.  Example:

	0 0 45 
	10 0 0

# Output Description

Your program should output the location of the enemy aircraft as a grid coordinate, a pair of numbers in X and Y positions - they may be floating point values. Example:

	10.0 10.0

# Challenge Inputs

	0 0 26.4
	11 7 343.4

----

	10 1 0.0
	2 8 352.82

----

	0 0 36.7
	10 1 336.42

# Challenge Outputs

	4 9
	10 9
	5 3 
