# Title

Elevator Scheduling

# Difficulty

Hard

# Description

Most of us have seen and ridden elevators - you crazy folks in the UK and commonwealth countries often call them "lifts" - but I'm sure I'm not the only one who has puzzled about the scheduling algorithms. Which riders do you pick up and when? Do you service requests in the order of arrival or do you work on maximal overlap?

For this challenge, you'll have to anwer those questions. You're designing an elevator scheduling algorithm for a building and you have plenty of riders to keep happy. 

# Input Description

You'll be given a single integer *N* on a line. The first *N* lines will identify elevator cars and with these fields: Car identifier, capacity, vertical speed in floors per second, and starting floor. Assume instantaneous getting on or off the elevator for the riders once you arrive on the floor. Assume that the elevator leaves with the rider as soon as it is able (e.g. it doesn't linger waiting for more people to arrive). 

Example:

	C1 12 .1 1

Then you'll get another integer on a line, *M*. The next *M* lines will show riders, with fields: Rider identification, elevator request time in seconds, source floor and destination floor. Rider identification numbers will be *stable*, meaning the rider will have the same identifier the entire exercise. Examples:

	R1 0 1 4

# Output Description

The main thing to show in the output is the time point at which all requests have been satisfied. (Yes, this is trying to get you guys to compete for the most efficient algorithm). Optionally show all intermediate steps and journeys, and wait times for riders. 

# Challenge Input

This was randomly generated, and so it has a few "oddities" in it, like riders who get on and off on the same floor, and riders who change their destination in the next second (e.g. in the middle of a ride). You still have to satisfy *every* request. 

	2
	C1 12 .1 1
	C2 12 .2 1
	201
	R12 3 1 8
	R13 16 1 9
	R6 23 1 3
	R4 26 1 9
	R14 36 1 9
	R15 41 1 3
	R11 42 1 3
	R10 42 1 8
	R1 62 1 9
	R17 66 1 11
	R2 70 1 3
	R16 72 1 4
	R17 74 11 9
	R0 80 1 11
	R1 84 9 7
	R5 85 1 11
	R16 85 4 1
	R0 87 11 12
	R19 88 1 9
	R1 98 7 11
	R1 100 11 2
	R1 109 2 7
	R16 113 1 6
	R0 118 12 9
	R5 120 11 8
	R2 121 3 11
	R3 127 1 11
	R15 127 3 7
	R16 128 6 11
	R10 129 8 1
	R6 130 3 10
	R18 141 1 8
	R7 145 1 9
	R16 150 11 2
	R5 161 8 2
	R2 161 11 3
	R1 162 7 7
	R19 163 9 7
	R5 169 2 1
	R4 170 9 3
	R7 172 9 12
	R2 172 3 4
	R17 174 9 4
	R10 186 1 7
	R7 194 12 7
	R4 197 3 9
	R17 198 4 9
	R17 208 9 8
	R10 213 7 3
	R9 214 1 7
	R7 222 7 1
	R11 226 3 2
	R7 236 1 12
	R7 238 12 8
	R10 239 3 7
	R17 241 8 8
	R0 247 9 10
	R18 248 8 1
	R1 250 7 5
	R17 263 8 5
	R8 274 1 11
	R11 290 2 1
	R13 290 9 12
	R7 293 8 9
	R2 304 4 11
	R6 309 10 8
	R2 312 11 9
	R0 315 10 8
	R18 325 1 9
	R13 350 12 6
	R13 354 6 10
	R3 356 11 3
	R17 382 5 3
	R7 384 9 1
	R3 390 3 9
	R15 393 7 4
	R3 397 9 10
	R12 397 8 10
	R18 399 9 2
	R9 403 7 12
	R1 409 5 11
	R9 410 12 2
	R16 415 2 1
	R10 416 7 8
	R17 423 3 7
	R2 426 9 2
	R8 428 11 5
	R8 431 5 2
	R3 432 10 7
	R0 433 8 12
	R12 440 10 1
	R17 442 7 9
	R13 444 10 3
	R5 452 1 3
	R7 462 1 7
	R16 466 1 2
	R15 468 4 5
	R17 481 9 12
	R12 492 1 1
	R11 498 1 3
	R8 505 2 1
	R17 507 12 1
	R8 509 1 8
	R0 513 12 1
	R15 516 5 5
	R8 517 8 1
	R0 521 1 8
	R0 522 8 5
	R6 535 8 12
	R5 537 3 11
	R3 539 7 2
	R0 546 5 10
	R17 558 1 5
	R16 560 2 10
	R18 576 2 3
	R4 577 9 7
	R2 587 2 10
	R7 588 7 7
	R19 591 7 2
	R1 598 11 10
	R6 600 12 4
	R11 604 3 2
	R14 609 9 6
	R4 610 7 10
	R15 610 5 4
	R4 628 10 8
	R6 629 4 3
	R16 632 10 10
	R13 632 3 7
	R13 634 7 2
	R2 637 10 10
	R15 650 4 8
	R16 650 10 9
	R3 659 2 9
	R2 661 10 5
	R11 661 2 4
	R17 672 5 7
	R5 674 11 1
	R2 674 5 11
	R13 678 2 3
	R10 682 8 6
	R19 683 2 3
	R9 685 2 2
	R7 697 7 10
	R11 714 4 5
	R14 715 6 12
	R1 717 10 11
	R10 725 6 12
	R10 726 12 11
	R14 730 12 5
	R11 731 5 5
	R0 737 10 6
	R14 739 5 11
	R12 741 1 12
	R6 742 3 2
	R12 742 12 11
	R10 751 11 11
	R17 755 7 4
	R16 756 9 4
	R19 760 3 12
	R18 771 3 9
	R4 802 8 6
	R1 808 11 4
	R12 820 11 2
	R5 832 1 8
	R17 841 4 8
	R13 841 3 6
	R5 842 8 3
	R3 843 9 1
	R17 846 8 9
	R6 857 2 12
	R12 862 2 7
	R16 866 4 7
	R9 877 2 9
	R12 880 7 6
	R6 884 12 11
	R6 885 11 3
	R12 885 6 2
	R18 888 9 10
	R13 892 6 11
	R7 893 10 12
	R15 897 8 6
	R4 905 6 6
	R8 907 1 1
	R1 926 4 12
	R10 928 11 4
	R13 932 11 11
	R6 934 3 3
	R16 936 7 11
	R3 943 1 4
	R19 955 12 12
	R17 956 9 11
	R4 964 6 11
	R7 967 12 4
	R6 973 3 8
	R2 976 11 3
	R11 977 5 12
	R2 978 3 9
	R14 986 11 1
	R17 987 11 8
	R8 999 1 2

# Code to generate rider input

    import random

    THRESH = 0.01
    FLOORS = 12

    class Rider(object):
        """docstring for Rider"""
        def __init__(self, name, floor):
            self.name = name
            self.rnd = random.Random()
            self.floor = floor
    
        def move(self):
            return self.rnd.random() <= THRESH
    
        def newfloor(self):
            old, self.floor = self.floor, self.rnd.randint(1, FLOORS)
            return '%s %s' % (old, self.floor)
    
        def __repr__(self):
            return '%s %%d %s' % (self.name, self.newfloor())
    
        def __str__(self):
            return self.__repr__()

    def main():
        riders = {}
        for r in range(20):
            riders['R%d' % r] = Rider('R%d' % r, 1)    
    
        for t in range(1000):
            for r in riders.values():
                if r.move():
                    print str(r).replace('%d', `t`)
