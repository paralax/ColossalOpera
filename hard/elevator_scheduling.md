# Title

Elevator Scheduling

# Difficulty

Hard

# Description

Most of us have seen and ridden elevators - you crazy folks in the UK and commonwealthy countries often call them "lifts" - but I'm sure I'm not the only one who has puzzled about the scheduling algorithms. Which riders do you pick up and when? Do you service requests in the order of arrival or do you work on maximal overlap?

For this challenge, you'll have to anwer those questions. You're designing an elevator scheduling algorithm for a building and you have plenty of riders to keep happy. 

# Input Description

The first few lines will identify elevator cars and with these fields: Car identifier, capacity, vertical speed in floors per second, and starting floor. Assume instantaneous getting on or off the elevator for the riders once you arrive on the floor. Assume that the elevator leaves with the rider as soon as it is able (e.g. it doesn't linger waiting for more people to arrive). 

Example:

	C1 12 .1 1

The next lines will show riders, with fields: Rider identification, elevator request time in seconds, source floor and destination floor. Examples:

	R1 0 1 4

# Output Description

The main thing to show in the output is the time point at which all requests have been satisfied. (Yes, this is trying to get you guys to compete for the most efficient algorithm). Optionally show all intermediate steps and journeys, and wait times for riders. 

# Challenge Input

	C1 12 .1 1
	C2 12 .1 1
	R1 0 1 4
	R2 2 1 5
	R3 2 1 6
	R4 6 1 8
	R5 9 1 3
	R1 10 4 2
	R2 12 5 8
	R6 20 1 9
	R7 22 1 6
	R8 29 1 9
