# Title

Ugly Christmas Sweater Knitting

# Difficulty 

Easy

# Description

Seeing as this time of the year some of you might be in the mood for something on the lighter side. Besides, isn't knitting the new cool thing that the kids are doing these days?    

Assaulting our loved ones'  senses with atrociously festive designs of the knit variety requires creativity and dedication. It's hard work, but somebody has to do it. A lot of vibrantly offensive patterns can be found on the internet; the only problem is that their textual descriptions are rarely consistent and are often confusing and pointlessly verbose.    

 I took it upon myself to come up with a simplified standard for a multicolor knitting pattern scheme, where a pattern is represented by sequences of expressions that can be easily processed by the human eye, as well as parsed by a program and printed out as a sketch. This makes the representation more descriptive and compact, with the added benefit of being able to make pattern changes on the fly and see the effects instantly, without the need to redraw the entire scheme.    

## Format description

1) Each row begins with an integer denoting the number of times the row must be repeated. The row count number is separated from the rest of the string by the "\#" symbol followed by a space, for example:    
    
    1# --&gt; repeat this row 1 time.    
    4# --&gt; repeat this row 4 times.   

2) The base sequence consists of a lowercase letter ([a-z]), followed by an asterisk ("\*") followed by an integer. A row can contain multiple base sequences (where different letters denote different colors), separated by a comma. For example, this expression      
 
    1# w*2, b*3, y*5   

means _repeat this row 1 time: make two white stitches, followed by three black stitches, followed by five yellow stitches_ ; represented in plain text, this gives the following scheme:  
 
     wwbbbyyyyy    
 
(note that letters are mere placeholders, you can map them to your own color scheme or ASCII symbols however you want)   

3) Groups and repetitions        

Some subsequences can be repeated a number of times. A group can consist of one or more base sequences, as well as other groups, contained in parentheses. A group is indicated by a "\*" sign that follows the parenthesis, and an integer denoting the number of repetitions. Groups can also be nested to an arbitrary depth. Example:   

    expression     
        2# (w*2, y*4)*2           
    makes this pattern scheme:                       
        wwyyyywwyyyy    
        wwyyyywwyyyy    

    example of a nested group:            
        1# ((b*5, w*2)*3, y*4)*2       
        bbbbbwwbbbbbwwbbbbbwwyyyybbbbbwwbbbbbwwbbbbbwwyyyy

4) Symmetry("mirroring" the sequence)    
Most [intarsia patterns](http://en.wikipedia.org/wiki/Intarsia_\(knitting\)) are symmetrical (right side mirrors left side - for example, a snowflake or a star). If a group needs to be repeated in reverse ("mirrored"), it is denoted by the "%" symbol followed by an integer:    

    1# (a*3, b*2)%2           
    aaabbbbaaa      

    1# (w*4, b*1)%3        
    wwwwbbwwwwwwwwb        

(note that when the number of reversals is greater than 2, the same subsequence is reversed again with each new repetition:       
    [wwwwb][bwwww][wwwwb])       

A row can contain a combination of both straight and reverse repetitions:       

    1# g*2, ((a*2, b*1, c*2)%2)*2, g*2
    ggaabccccbaaaabccccbaagg   

# Input Description       

A text file containing a pattern in the described format. I made a few simple patterns that can be found here    

https://gist.github.com/dvakota/94ae5e80854f02132691    
     
(For these files, assume all input is valid)  

You can also come up with patterns of your own -  the more obnoxious the better. Go nuts. Tis the season, after all :]     

# Output Description           

The scheme, or a "sketch" of the processed file/files, either in color or ASCII art. Don't forget to reference the source pattern.    

Samples of the generated sketches:    

https://github.com/dvakota/Toys/blob/master/dvakota/toys/sweater/generated-samples.txt    


# Notes

Many thanks to Redditor /u/katyne for this submission to /r/dailyprogrammer_ideas. If you have any ideas, please submit them there!      

