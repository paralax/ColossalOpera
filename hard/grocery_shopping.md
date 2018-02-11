# Title

Buying Groceries

# Difficulty

Hard

# Description

You walk into a grocery store with some money in your wallet, a target amount of food to buy, and one bag with a finite capacity. Identify what you can buy under those conditions. You have to buy at least a quarter pound of any one thing.

# Input Description

You'll be given a row with three numbers on it representing the bag capacity in pounds, your budget in dollars, and the target calorie count for the week. Then you'll be given a series of items showing the item, its calories per pound and its price per pound. Example:

    10 100.00 14000
    Ham 600 9.00

This translates to a bag that can hold ten pounds, a $100 bill in your wallet, and a target calorie count of 14000 for the week (seven * 2000). Second, you can buy some ham for $9 a pound and get 600 calories per pound. 

All foods *should* be one word, hopefully cut and paste didn't foul that up.

# Output Description

Your program should emit one or more solutions for the shopping trip.

# Challenge Input

    10 100.00 14000
    Ham 650 8.50
    Lettuce 70 0.75
    Cheese 1670 6.00
    Tuna 830 20.00
    Bread 1300 1.20
    Eggs 200 4.25
    Milk 130 4.00
    Yogurt 475 3.75
    Sugar 936 2.00
    Oil 3200 3.50
    Cereal 700 5.25
    Chicken 500 3.00
    Raisins 1776 5.00
    Bananas 160 1.10
    Grapes 90 4.00
    Mango 85 1.25
    Cherries 80 6.00
    Pears 68 4.00
    Apples 55 3.00
    Pineapple 51 4.00
    Oranges 48 6.00
    Plums 43 6.00
    OrangeJuice 41 4.50
    Grapefruit 39 3.00
    Berries 37 2.50
    Papaya 30 2.75
    Peaches 30 2.25
    Honeydew 26 3.00
    Cantaloupe 23 3.00
    Strawberries 20 2.75
    Watermelon 18 1.75

# Credit

The idea for this challenge was taken from [this interview summary](http://www.jasq.org/just-another-scala-quant/new-agey-interviews-at-the-grocery-startup)
