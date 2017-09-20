# Title

Training for Summiting Everest

# Difficulty

Intermediate

# Tags

subsequence

# Description

You and your friend wish to summit Mount Everest the highest peak in the world. One problem: you live at sea level and despite being in great shape haven't been at altitude very long. So you propose a series of stays on mountaintops around the world using increasing elevations to prepare your body for the extremes you'll encounter. 

You and your friend gather a list of mountain peaks that you'd like to visit on your way there. You can't deviate from your path but you can choose to go up the mountain or not. But you have to pick ones that go higher than the previous one. If you go _down_ your body will suffer and your trip to the summit of Everest will be in peril.

Your friend has done the job of lining up the route to get you from home to basecamp. She looks to you to devise an algorithm to pick the peaks to summit along the way maximizing your summits but always going higher and higher never lower than you did before. 

Can you devise such an algorithm such that you find the list of peaks to summit along the way? Remember - each has to be higher than the last you want to hit as many such peaks as possible and there's no turning back to visit a previously passed peak.

# Input Description

You'll be given a series of integers on a line representing the peak height (in thousands of feet) that you'll pass on your way to Everest. Example:

	0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15

# Output Description

Your program should emit the peak height you should summit in order that are always higher than the previous peak. Example:

	0 2 6 9 11 15

# Challenge Inputs

	1 2 2 5 9 5 4 4 1 6
	4 9 4 9 9 8 2 9 0 1
	0 5 4 6 9 1 7 6 7 8
	1 2 20 13 6 15 16 0 7 9 4 0 4 6 7 8 10 18 14 10 17 15 19 0 4 2 12 6 10 5 12 2 1 7 12 12 10 8 9 2 20 19 20 17 5 19 0 11 5 20

# Challenge Output

	1 2 4 6
	4 8 9
	0 1 6 7 8
	1 2 4 6 7 8 10 14 15 17 19 20
