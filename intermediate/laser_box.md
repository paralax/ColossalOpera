# Title 

Laser in a Box

# Difficulty

Intermediate

# Tags

ASCII art

# Description

Today's challenge is based on ASCII art, boxes, and lasers. Simply put, can you trace the path of a laser in a rectangular box, assuming it's coated with mirrors inside? 

In this case, lasers will start in the upper left corner of the box and be made of only `/` or `\`. You should assume a perfect bounce off the side of the box. 

# Input Description

You'll be given two integers, *n* and *m*, representing the width and heigth of the box to build. Example:

5 3

# Output Description

Your program should emit the box with the full path of the laser traced. Example:

    #######
	#\/\/\#
	#/\/\/#
	#\/\/\#
    #######

# Challenge Input

	2 2
	22 6
	6 3

# Challenge Output

	####
	#\ #
	# \#
	####

	########################
	#\  /\  /\  /\  /\  /\ #
	# \/  \/  \/  \/  \/  \#
	# /\  /\  /\  /\  /\  /#
	#/  \/  \/  \/  \/  \/ #
	#\  /\  /\  /\  /\  /\ #
	# \/  \/  \/  \/  \/  \#
	########################

	########
	#\    /#
	# \  / #
	#  \/  #
	########
