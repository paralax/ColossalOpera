# Title

Finding Ancestors

# Difficulty

Intermediate

# Description

Given a body of facts, can you answer a question about who is someone's grandparent?

# Input Description

You'll be given a set of names, all unique. The parentage and lineage of people is shown; for instance, A+B=C means A and B had a child C. Multiple children will be separated by a comma. For Example:

    1
    Beth+Dave=Tom,Dick,Harry

Then you'll be given a person's name followed by one or more question marks or exclamation points. Each question mark means go back one level of ancestery, each exclamation mark means go *forward* one level of ancestery. For example:

    2
    Beth!
    Harry?

# Output Description

Your task is to find one or more ancestors (or descendants) of that person at the correct level. From our example:

    Beth->Tom,Dick,Harry
    Harry<-Beth,Dave

# Challenge Input

    8
    Beth+Dave=Tom,Dick,Harry
    Jan+John=Mary,Michael,Amy
    Amy+Harry=Jim,John,Joe
    Mary+Dick=Bill
    Joan+Tom=Sam
    Sam+Jane=Larry,Peter
    Peter+Pauline=Francine
    Francine+Frank=Thomas
    4
    Peter??
    Sam!!
    Thomas??
    Francine??
    Beth!!!

# Challenge Output

    Peter<-Joan,Tom,Tom,Jane