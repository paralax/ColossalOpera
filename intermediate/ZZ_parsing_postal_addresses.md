# Title

[2017-07-12] Challenge #323 [Intermediate] Parsing Postal Addresses

# Difficulty

Intermediate

# Tags

text parsing

# Description

Nealy everyone is familiar with mailing addresses - typically a person, optionally an organization, a street address or a postal box, a city, state or province, country, and a postal code. A practical bit of code to have is something that parses addresses, perhaps for validation or for shipping cost calculations. 

Today's challenge is to parse addresses into some sort of data structure - an object (if you're using an OOP language), a record, a struct, etc. You should label the fields as correctly or appropriately as possible, and map them into a reasonable structure. Not all fields will be present, so you'll want to look over the challenge input first and design your data structure appropriately. Note that these include international addresses. 

# Input Description

You'll be given an address, one per multi-line block. Example:

    Tudor City Greens
    24-38 Tudor City Pl
    New York, NY 
    10017
    USA

# Output Description

Your program should emit a labeled data structure representing the address. From the above example:

    business=Tudor City Greens
    address=24-38
    street=Tudor City Pl
    city=New York
    state=NY
    postal_code=10017
    country=USA

Your field names may differ but you get the idea. 

# Challenge Input

    Docks
    633 3rd Ave
    New York, NY 
    10017
    USA
    (212) 986-8080

    Hotel Hans Egede
    Aqqusinersuaq
    Nuuk 3900
    Greenland
    +299 32 42 22

    Alex Bergman
    Wilhelmgalerie
    Platz der Einheit 14
    14467 Potsdam
    Germany
    +49 331 200900

    Dr KS Krishnan Marg
    South Patel Nagar
    Pusa
    New Delhi, Delhi 
    110012
    India

