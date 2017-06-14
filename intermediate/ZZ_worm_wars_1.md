# Title

[2016-06-14] Challenge #319 [Intermediate] Worm Wars 1 - Basic Epidemiology

# Difficulty

Intermediate

# Tags

epidemiology, dynamic systems

# Description

This is inspired in part by recent WannaCry malware propagation as well as some work I did a long time ago into worm propagation models. I figured it would make a fun pair of challenges. This was further influenced by a recent 2D Game of Life challenge. 

For basic computer worm propagation models, a lot of focus historically has been on the standard SIR model from epidemiology. Using mathematical models and treating the computer worm as a pathogen, basic simulations ignore a lot of complexities to begin to answer some fundamental questions using mathematical epidemiology to model the establishment and spread of those pathogens. 

As part of this approach, populations are tracked in multiple buckets to track their states. The SIR model, a fundamental model in such systems, labels these three compartments S = number susceptible, I =number infectious, and R =number recovered (immune):

- S - able to be infected by the pathogen
- I - currently infected and spreading the pathogen
- R - immune from the pathogen (e.g. recovered)

The population is therefore the sum of these three buckets, which change over time. In theory for a new pathogen everyone starts out in state *S*, and either becomes *I* if they get hit with the pathogen first or *R* if they get immunized (patched). Alternatively once infected they can recover. Each transition - S -> I, I -> R, and S -> R - have their transition rates. You can assume no back transitions - you won't see I -> S or R -> I, for example. 

Your challenge today is to model a basic epidemiological system. Given a population and some transition rates, model some number N of generations. 

# Input Description

You'll be given some values on a line telling you the total population size (N), the initial population seed of infected systems (I), and then transition rates for S to I, I to R and S to R. Example:

	10000 10 0.01 0.01 0.015

You have 10000 systems to track, 10 of which are infected, and S -> I is 0.01, I -> R is 0.01, and S -> R (those that get patched first) is 0.015. 

# Output Description

Your program can emit answers in a number of different ways:

- Graphical - show S I and R populations over time (as total or fractions)
- Textual - a huuuuge list of numbers
- Other - be creative

# Challenge Input

	   10758 21 0.051 0.930 0.178
	   18450 12 0.320 0.969 0.306
	   9337 15 0.512 0.513 0.984

# Bonus

Additional lines will tell you new timepoints at which the parameters change. For instance a more virulant strain of the malware becomes available, or a patch gets released. These lines will contain the format of timestep T, then updated transition rates for S to I, I to R and S to R. From the above example:

	10000 10 0.01 0.01 0.015
	100 0.02 0.01 0.015
	200 0.02 0.03 0.03

This model can allow you to test the effects of various changes on malware propagation - faster patching, more virulent worms, larger seed populations, etc. 
