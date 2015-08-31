# Title

Broken Keyboard

# Difficulty

Easy

# Description

Help! My keyboard is broken, only a few keys work any more. If I tell you what keys work, can you tell me what words I can write?

(You should use the trusty enable1.txt file, or `/usr/share/dict/words` to chose your valid English words from.)

# Input Description

You'll be given a line with a single integer on it, telling you how many lines to read. Then you'll be given that many lines, each line a list of letters representing the keys that work on my keyboard. Example:

    3
    abcd
    qwer
    hjklo

# Output Description

Your program should emit a list of words for each keyboard configuration. 

    abcd = a aa aba abac abaca abb acca ad adad add adda b ba baa baba bac bacaba bacca bad c ca cab caba cabda cad d da dab dabb dabba dad dada
    qwer = e eer er ere err ewe ewer ewerer q qere r re ree reree w we wee wer were
    hjklo = h ho holl hollo hook j jhool jo joll k ko kohl koko kolo kolokolo l lo loll loo look o oh oho

# Challenge Input

    4
    edcf
    bnik
    poil
    vybu

# Challenge Output

    edcf = c ce cede cee d de dee deed deedeed e f fe fed fee feed
    bnik = b bib bibb bibi bikini bin bink i in ink inn k kiki kin kink n ni nib
    poil = i ill io ipil l li lill lip lo loll lollipop lollop loo loop lop o oii oil olio p pi pili pililloo pill pip pipi plop po poi poil pol polio poll polloi polo pool pooli poop pop
    vybu = b bu bub bubby buy by u v y

# Scala solution

Uses regexes

    def typewriter(keys:String): String = words.filter(("[" + keys + "]+").r.replaceAllIn(_,"")=="").mkString(" ")