# Title

Write a JSON Serializer

# Difficulty

Intermediate

# Description

You've just been hired at a particularly awful software company. One of the reasons that makes them so awful is that importing libraries is a fire-able offense.

None of your coworkers have any idea what serializing is, and to stand out you want to serialize your data before writing to disk. Because you aren't allowed to import libraries, you'll have to write it yourself.

You've chosen to use JSON for serialization due to ease of use, and the fact that it already represents the objects you use pretty well! Not to mention the fancy flow charts on the [JSON website](http://json.org/).

# Formal Inputs & Outputs

## Input Description:

As your first project, you must convert the company's proprietary non-escaped format into properly escaped JSON. On every line, they write out the hierarchy to reach each value, with the value on the end. Arrays have multiple values with the same hierarchy.

## Output Description

A JSON representation of the input

# Sample Inputs & Outputs

## Input

    Fruits:Apple:Red
    Fruits:Banana:Yellow
    Vegetable:Broccoli:15
    Clothes:Shirt
    Clothes:Pants
    Clothes:Shoes

## Output

    {"Clothes":["Shirt","Pants","Shoes"],"Fruits":{"Apple":"Red","Banana":"Yellow"},"Vegetable":{"Broccoli":15}}

# Bonus Challenge

Pretty-print your output

# Notes

Many thanks to Redditor /u/G33kDude for this submission to /r/dailyprogrammer_ideas. If you have any ideas, please submit them there!