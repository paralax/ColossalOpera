# Title

Unique County Names

# Difficulty

Intermediate

# Description

In the United States, states are divided first into counties (or in the case of Louisiana *parishes*, in Alaska *minicipalities*, *census areas* or *boroughs*, and in the US territory Puerto Rico *municipios*) before being further divided into smaller chunks of land and then finally cities, towns and villages. A great number of these counties have common names (e.g. for US presidents), but even more have local and historic names such as native tribes. 

In this challenge, you're looking for those unique names. A couple of things to note:

- You can ignore the *type* of division it is, such as a county, city or parish. For comparisons, focus only on the **name** (e.g. Polk County would be the same as Polk Parish).
- Some of them have two word names (e.g. Prince William County), treat that as the name (Prince William). 
- Yes, this is part data munging because of the complexity of the data source - human names.
- Yes, there will be many, many unique names. That's part of the challenge. 
- Focus only on the 50 US states, so ignore Puerto Rico, DC, etc. The data set includes extra territories, so you'll have to analyze it first to discover which ones to omit. 

The data comes from the US Census Bureau and can be downloaded from this URL: http://www2.census.gov/geo/docs/reference/codes/files/national_county.txt 

# Input Description

You'll find that the website formatted the data in CSV. An example line is:

    AL,01,001,Autauga County,H1

We only care about the first and fourth columns, so in this case "AL" and "Autauga County". If you want to know more about the data, it's the [2010 FIPS Codes for Counties and County Equivalent Entities](https://www.census.gov/geo/reference/codes/cou.html), see that site for a full explanation. 

# Output Description

Your program should emit the unique county (or county equivalent) name as pairs of abbreviated state name (e.g. "AL") and county name (e.g. "Polk County") for the 50 US states. 
