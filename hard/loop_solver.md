# Title

Loop Puzzle Solver

# Difficulty

Hard

# Tags

puzzle

# Description

The New York Times magazine recently (as of late 2015) introduced a new puzzle at the back of the magazine, dubbed "Loop". In the puzzle, you're given a grid with one or more squares blocked off, and one or more squares with a circle in it. To solve the puzze, you have to draw a continuous line - the loop - through the squares but there are some constraints:

- The loop has to visit every non-blocked cell exactly once
- The loop has to proceed across, up or down, never diagonally. You can enter a grid square on one side and leave on any of the other three.
- The loop must go through cells marked with a circle straight across, with no turn

Your challenge today is to implement a solver for a loop puzzle.

# Input Description

You'll be given an ASCII grid showing you the empty squares as underscores, the blocked off squares marked with a hash mark, and the circle grid squares with a lowercase `o`. Example:

        _ _ # _ _
        _ _ o _ _
        _ _ _ _ _
        # _ _ _ _

# Output Description

Your program should emit the ASCII art grid with the loop drawn in. For up and down, use a pipe `|`, for ascross use a dash `-`, and for a turn use a plus `+`; use the spaces in the input square to fill in the final parts of the loop (e.g. the dashes `-`). For the circle, it's show the line in the normal gap on either side and leave the circle in place. Example:

    +-+ # +-+
    | +-o-+ |
    +-+ +-+ |
    # +-+ +-+

By filling in the gap columns we can more easily see the loop we drew.

# Challenge Input

    _ _ # _ _ _ _ _ _ _
    _ _ _ _ _ _ _ _ _ _
    o _ _ _ _ _ _ o _ _
    _ # _ _ _ _ _ _ o o
    _ _ _ _ _ _ _ _ _ _
    _ o # _ _ _ _ o _ _ 
    _ _ o _ _ _ o _ _ _ 
    _ _ _ _ # _ _ _ _ _

# Challenge Solution

    +-+ # +-----------+
    | | +-+ +---+ +-+ |
    o +-+ +-+ +-+ o | |
    | # +-+ +-+ +-+ o o
    | +-+ +-+ +-+ +-+ |
    | 0 # +-+ +-+ o +-+
    | +-o-+ +-+ o | +-+ 
    +-----+ # +-+ +---+

