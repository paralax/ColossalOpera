# Title

Generating Text with Markov Processes

# Difficulty

Intermediate

# Tags

Markov, text generation

# Description

Text generation algorithms exist in a wide variety of formats, including "Mad Libs" and Markov processes. A Markov chain algorithm generates text by creating a statistical model of potential textual suffixes for a given prefix. That's a fancy way of saying "it basically determines the next most probable word given the training set." Markov chain programs typically do this by breaking the input text into a series of words, then by sliding along them in some fixed sized window, storing the first N-1 words as a prefix and then the Nth word as a member of a set to choose from randomly for the suffix. Then, given a prefix, pick randomly from the suffixes to make the next piece of the chain. 

Take this example text:

    Now is not the time for desert, now is the time for dinner 

For a set of triples, yielding a bi-gram (2 word) prefix, we will generate the following prefixes and suffix:

    Prefixes        Suffixes
    --------        --------
    Now, is         not
    is, not         the
    not, the        time
    the, time       for
    time, for       desert
    for, desert     now
    desert, now     is
    now, is         not, the  
    is, the         time
    the, time       for
    time, for       desert, dinner

You'll see a couple of the prefixes have TWO suffixes, this is because they repeat but one with a different suffix and one with the same suffix. Repeating this over piles and piles of text will start to enable you to build statistically real but logically meaningless sentences. Take this example output from my program after running it over Star Trek plot summaries:

    "attack." In fact, Yeoman Tamura's tricorder shows that Kirk has been killed after
    beaming down to the bridge, Kirk reminisces about having time to beam down. Kirk wants
    Spock to grab hold of him in a fist fight with Kirk and Spock try to escape, the collars
    are activated, subjecting them to an entrance, which then opens. Scotty saves the day by
    pretending to help Spock, and Mullhall voluntarily agree, and the others transported to
    the one which is not at all obvious what to make diplomatic advances. Meanwhile Kirk is
    able to get inside. McCoy and nerve pinches Chief at

# Challenge

Your challenge today is to implement a Markov generator supporting a bi-gram prefix. It should be capable of ingesting a body of text for training and output a body of text generated from that. 

# Notes

[Markov Chain Algorithm](http://www.rose-hulman.edu/Users/faculty/young/CS-Classes/csse220/200820/web/Programs/Markov/markov.html) from rose-hulman.edu

# Python Solution

This is based on the example from Kernighan and Pike's The Practice of Programming, chapter 3.

    from itertools import islice
    import random
    import sys

    class Markov(object):
        def __init__(self, open_file):
            self.cache = {}
            self.open_file = open_file
            self.words = self.file_to_words()
            self.word_size = len(self.words)
            self.database()

        def file_to_words(self):
            self.open_file.seek(0)
            data = self.open_file.read()
            words = list(filter(None, data.split()))
            return words

        def window(self, seq, n=3):
            "Returns a sliding window (of width n) over data from the iterable"
            "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
            # from https://docs.python.org/release/2.3.5/lib/itertools-example.html
            it = iter(seq)
            result = tuple(islice(it, n))
            if len(result) == n:
                yield result    
            for elem in it:
                result = result[1:] + (elem,)
                yield result

        def database(self):
            for w1, w2, w3 in self.window(self.words, n=3):
                key = (w1, w2)
                if key in self.cache:
                    self.cache[key].append(w3)
                else: 
                    self.cache[key] = [w3]

        def generate_markov_text(self, size=25):
            seed = random.randint(0, self.word_size-3)
            w1, w2 = self.words[seed], self.words[seed+1]
            gen_words = []
            for i in range(size):
                gen_words.append(w1)
                try:
                    w1, w2 = w2, random.choice(self.cache[(w1, w2)])
                except:
                    pass
            gen_words.append(w2)
            return ' '.join(gen_words)

    if __name__ == '__main__':    
        for arg in sys.argv[1:]:
            m = Markov(open(sys.argv[1], 'r'))
            print(m.generate_markov_text(100))
            del(m)
