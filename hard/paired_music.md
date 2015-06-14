# Title

Pairs of Musical Artists

# Difficulty

Hard

# Description

Like many of you, I've more or less ditched my MP3 collection in favor of streaming services. I have tons of playlist sfor every setting (work, play, etc). A lot of these services use the co-occurrence of entries to make suggestions. 

For this challenge, you'll look at playlist artists and try and identify co-occurrence of artists, which may be useful for a recommender system. 

# Input Description

You'll be given a set of 1000 rows, with each row a unique playlist and the artists from their playlists separated by commas. For example:

    Radiohead,Pulp,Morrissey,Delays,Stereophonics,Blur,Suede,Sleeper,The La's,Super Furry Animals
    Band of Horses,Iggy Pop,The Velvet Underground,Radiohead,The Decemberists,Morrissey,Television etc.

# Output Description

Your program should emit the list of musical artists who appear together in at least fifty (50) different playlists. From the above example:

    Radiohead + Morrissey

# Challenge Input

The data is available via Github here: https://gist.github.com/paralax/f2bba6dbe1aa51693ba1 


# Notes

Shamelessly stolen from https://github.com/sming/Shapeways via http://www.reddit.com/r/compsci/comments/39orbc/i_failed_a_code_test_how_would_you_solve_this/ 