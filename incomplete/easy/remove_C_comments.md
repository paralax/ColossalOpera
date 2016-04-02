# Title

Remove Comments from C Code

# Difficulty

Easy

# Description

The C programming language supports comments of two types:

* single line comments beginning with `//`
* multiline comments enclosed in `/*` and ending with `*/`

Examples include:

    // This is a simple single-line comment

An example of a multiline comment

    /*
     * This is a lengthy multiple-line comment that 
     * wraps into the next line
     */

An example of multiple single line comments in a structure:

    struct foo {
            struct foo      *next;          /* List of active foo. */
            struct mumble   amumble;        /* Comment for mumble. */
            int             bar;            /* Try to align the comments. */
            struct verylongtypename *baz;   /* Won't fit in 2 tabs. */
    };
    struct foo *foohead;                    /* Head of global foo list. */


Your input program will be:

    #include <stdio.h>

    /*
     * All major routines should have a comment briefly describing what
     * they do.  The comment before the "main" routine should describe
     * what the program does.
     */

    // foo!
    int main(int argc, char *argv[]) {
            /* this is simple isn't it? */
            printf("hello world\n");
            /* can you handle these? */ printf("Hello again!\n");
            return(1);
    }


# Output
    
You program should emit:

    int main(int argc, char *argv[]) {
        printf("hello world\n");
        printf("Hello again!\n");
        return(1);
    }

# Bonus

Write your program so that it can also handle other language comments, like Java (// -> newline), BASIC ("rem" -> newline), m4 (dnl -> newline), or even OCaml ( `//` and `(*` to `*)`). 

# Notes

This challenge was suggested by /u/frozensunshine.  Have a good challenge idea? Consider submitting it to /r/dailyprogrammer_ideasd