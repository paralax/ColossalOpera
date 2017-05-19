# Title

Worm Wars 2 - Network Epidemiology

# Difficulty

Hard

# Tags

epidemiology, dynamic systems

# Description

This one builds on the previous challenge: malware propagation. But now we add a twist - network topology, specifically connectivity and congestion.

Real world network malware can't attack a host it can't connect to. That connection may be blocked due to a lack of connectivity between the host (e.g. not directly connected networks), or a congested pipe. Network connections get congested when they're flooded with traffic, forcing packet loss. 

For today's challenge, you're being asked to model a small network in which some malware has been introduced. , but the . Work with these assumptions:

- To spread the malware has to send a single packet of size B and takes 1 time step
- The network has fixed capacity between subnets
- If you try and send a packet over a pipe at 95% utilization or above it gets dropped
- Propagation between two hosts can only occur if they can directly connect from network to network
- An infected host can only send one packet at a time
- Assume the standard SIR model from last time

# Input Description

You'll be given a lot of information for this one. First an integer on one line telling you how many networks to read. For each network specification you'll have a line telling you the network ID (a letter), the number of hosts in it (N), the number of infected hosts at time 0 (I). Then another integer telling you how many links to read. Then that many lines telling you what two networks connect and with what capacity in bytes per second (assume symmetric connections). Finally for the malware you'll be given some values on a line telling you the transition rates for S to I, I to R and S to R. Finally a line with a single integer, B, telling you the size of the malware propagation packet (assume UDP, so a single packet to infect). Example:

	10
	A 1000 1 
	B 1000 0
	C 1000 3
	D 1000 0
	E 1000 0
	F 1000 1
	G 1000 10
	H 1000 0
	I 1000 0
	J 1000 90
	10
	A B 10000
	B C 1000
	C D 2000
	D E 2000
	D F 2000
	D G 5000
	D H 9000
	D I 1000
	D H 8000
	D J 10000
	0.01 0.01 0.015
	256

# Output Description

Your program can emit answers in a number of different ways:

- Graphical - show S I and R populations over time (as total or fractions)
- Textual - a huuuuge list of numbers
- Other - be creative
