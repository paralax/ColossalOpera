# Title

Preparing for the Demon Lord

# Difficulty

Easy

# Description

You are a combat analyst for the chosen band of heroes that will overthrow the tyranny of the Demon Lord. The fated battle is but mere months away, so it is crucial that the heroes be as prepared as possible.

As part of this preparation, you are required to analyze some of the heroes' past combat records in order to help guide future training.

# Formal Inputs & Outputs

## Input description

You will be provided with a number M, followed by a list of the names of the M combatants. Then, the number N, followed by a list of N events.

Events will be of the form:

<combatant>,<"INFLICTED" or "RECEIVED">,<damage>

Where "INFLICTED" indicates that the combatant dealt damage, and "RECEIVED" indicates that the combatant received damage.

You can be sure that for the input provided that M will be >= 1, that there will be at least one "INFLICTED" and one "RECEIVED" event, and that damage will be >= 0. You can also be sure that no lines will be > 60 characters. You're welcome to make your solution handle these inputs if you like though!

## Output description

You should output the combatant(s) who inflicted the most amount of damage, those who received the most amount of damage, and those who were involved in the most number of events.

# Sample Inputs and Outputs

## Sample Input

A basic input to get you started.

    3
    Chosen One
    The Min-maxer
    Secret Antagonist
    10
    Chosen One,RECEIVED,13
    Chosen One,RECEIVED,6
    Secret Antagonist,INFLICTED,8
    Chosen One,INFLICTED,4
    The Min-maxer,INFLICTED,16
    The Min-maxer,RECEIVED,3
    Secret Antagonist,INFLICTED,16
    The Min-maxer,RECEIVED,5
    Secret Antagonist,INFLICTED,15
    Secret Antagonist,RECEIVED,11
    
## Sample Output

    Most Damage Dealt (39): Secret Antagonist
    Most Damage Taken (19): Chosen One
    Most Events Involved With (4): Secret Antagonist
    
## Sample Input

This one tests for multiple combatants fulfilling the maximum condition.

    3
    Hero of Legend
    The Lone Wolf
    Disguised Demon Lord
    10
    Hero of Legend,RECEIVED,16
    The Lone Wolf,INFLICTED,14
    Disguised Demon Lord,RECEIVED,16
    The Lone Wolf,INFLICTED,16
    Disguised Demon Lord,RECEIVED,10
    Disguised Demon Lord,RECEIVED,7
    Hero of Legend,INFLICTED,14
    Disguised Demon Lord,INFLICTED,13
    Disguised Demon Lord,RECEIVED,2
    Hero of Legend,RECEIVED,19
    
## Sample Output

    Most Damage Dealt (30): The Lone Wolf
    Most Damage Taken (35): Disguised Demon Lord, Hero of Legend
    Most Events Involved With (5): Disguised Demon Lord
    
## Sample Input

Here's a link to a [gist](https://gist.github.com/nichwn/9e055cb3a8504f13c682) with 1000 actions.

## Sample Output

    Most Damage Dealt (1038): Childhood Friend
    Most Damage Taken (1097): Animal Familiar
    Most Events Involved With (208): Animal Familiar, The Chosen One

# Notes

Many thanks to Redditor /u/oketa for this submission to /r/dailyprogrammer_ideas. If you have any ideas, please submit them there!