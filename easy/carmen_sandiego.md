# Title

Carmen Sandiego and her Gang 

# Difficulty

Easy

# Description

You've been tasked with assisting interpol in catching Carmen's gang. To make things easier the detectives want to enter characteristics of the crime scene and narrow down which known criminals are most likely to have been involved in a theft. 

Your job is to write a database which stores attributes about a known criminal. Each record will be input as a line formatted as follows:


    <N, the number of records to be input>
    <Name>|<Attribute>
    ...
    <Name>|<Attribute>
    

After you've stored the known attributes of the known suspects, your program should accept a list of attributes form the crime scene and filter down the list of suspects to seed up the investigation.

The list of attributes will be formatted like this:


    <N, the number of attributes to filter on>
    <Attribute 1>
    ...
    <Attribute N>


# Bonus Challenge 1

Given a log from the crime scene formatted as a list of notes from the detectives such as:

> The suspect drove off in a fast car

Your program should find the known attribute 'fast car' (which is a known clue) and look at only suspects with fast cars.

# Database Input

    46
    Justin Case|painting
    Justin Case|Holland
    Justin Case|black hair
    Justin Case|blue eyes
    Justin Case|lawyer
    Justin Case|male
    Contessa|Italian
    Contessa|Italy
    Contessa|Milan
    Contessa|fashion
    Contessa|female
    Eartha Brute|green hair
    Eartha Brute|pink uniform
    Eartha Brute|gold belt
    Eartha Brute|romantic
    Eartha Brute|chewing granite
    Eartha Brute|house tossing
    Eartha Brute|female
    Kneemoi|extraterrestrial
    Kneemoi|planet Roddenberry
    Kneemoi|green skin
    Kneemoi|big head
    Kneemoi|flying saucer
    Sarah Nade|piano
    Sarah Nade|rocker
    Sarah Nade|musician
    Sarah Nade|scar on her left ear
    Sarah Nade|blonde hair
    Sarah Nade|green eyes
    Sarah Nade|female
    Patty Larceny|teenager
    Patty Larceny|female
    Patty Larceny|fashion
    Patty Larceny|blue eyes
    Top Grunge|biker
    Top Grunge|bad attitude
    Top Grunge|dirty
    Top Grunge|male
    Top Grunge|sunglasses
    Vic the Slick|salesman
    Vic the Slick|male
    Vic the Slick|moustache
    Vic the Slick|polyester suit
    Vic the Slick|ugly tie
    Vic the Slick|blue eyes
    Sir Vile|evil knight
    Sir Vile|armor
    Sir Vile|bad mood
    Sir Vile|fire-breathing
    Sir Vile|male


# Clues from Crimes

* Crime 1:

        3
        female
        fashion
        green eyes
    
* Crime 2:

        3
        male
        blue eyes
        Holland    

* Crime 3:

        1
        male
    
# Bonus Crimes

* Crime 1

    > A witness noticed an angry, green eyed, knight stealing round tables from the Louvre.

* Crime 2

    > A witness noticed a woman stealing fashion accessories from a designer in Italy.
    
    > The women wore a red dress.

# Notes

Many thanks to Redditor /u/EPYJAO for this submission to /r/dailyprogrammer_ideas. If you have any ideas, please submit them there!