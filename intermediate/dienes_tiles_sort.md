# Title

Sorting Dienes Tiles

# Difficulty

Intermediate

# Tags

combinatorics

# Description

One of the common features of mathematical education across the world is the use of *manipulatives*, or physical objects that help students (especially young students) develop familiarity with mathematical concepts. Among the many researchers who worked in this field is the late Hungarian mathematician [Zoltan Dienes](http://www.zoltandienes.com/). One of the tools he used to teach combinatorics were Dienes Tiles made of wood or plastic. 

Tiles have four properties:

- color - one of red (R), yellow (Y), or blue (B)
- shape - one of box (X), diamond (N), circle (C), or triangle (T)
- pattern - closed (P) or open (O)
- size - big (G) or small (L)

When a child works with these tiles, one of the lessons is to sort them into a line such that any two adjacent tiles have only one difference (e.g. size). As lessons progress you get into other arrangements like graphs, loops, and meshes. 

Your task today is to write a program that can sort the above tiles into a long line. 

# Input Description

The tiles will be given to you as a randomly sorted set of inputs over multiple lines. All 48 tiles are there.

# Output Description

Your program should emit an arrangement of tiles that satisfies the child's assignment - no two adjacent tiles have more than one difference. Aside from that one constraint, any resulting order will do - i.e. you can start with any tile you wish. Tiles may be used only once. 

# Challenge Input

    RXOL RNOL YXOG BXPL BTOL RNOG BTPL RTOG RCOL RXPL RTPG YNOL BNOG RXPG BXPG BXOL BCOG YTOL YXOL YCPL 
    BXOG RTPL BCOL YTOG YTPL YCPG YCOL YXPG RCPG RNPG YNPG YTPG YNPL BNOL RXOG BNPG BCPG YXPL BNPL BCPL 
    RCPL RTOL YCOG BTOG RNPL YNOG BTPG RCOG

# Bonus Challenge

Other assignments that the students work on with the tiles as time goes on include subsets that form a special arrangement. One such arrangement is a loop of *N* spots. The child has to pick out tiles and arrange them in a loop to fulfil the requirements, only the head and tail of the loop have to come together too. 

Write a program that can arrange some number *N* of the above tiles into a closed loop to satisfy the arrangement requirements. 

# FSharp Solution

No bonus attempted.

    let hamming (a:string) (b:string) : int =
        Array.zip (a.ToCharArray()) (b.ToCharArray()) |> Array.filter (fun (x,y) -> x <> y) |> Array.length
    let closest (t:string) (ts:string list) : string =
        List.map (fun x -> (hamming t x, x)) ts |> List.sort |> List.map snd |> List.head 
    let remove (t:string) (ts:string list) : string list =  List.filter (fun x -> x <> t) ts
    let sort (ts:string list) : string list =
        let rec _sort(ts:string list) (acc:string list) : string list =
            match ts with
            | []    -> acc
            | _ ->  let c = closest (List.head acc) ts
                    let cs = remove c ts
                    _sort cs (c::acc)
        _sort (List.tail ts) [(List.head ts)]

    let tiles =   ["YCOG"; "RCPL"; "BXPG"; "YNPG"; "YNOG"; "RXOL"; "BCOL"; "YXOG"; "RTOG";
       "RCPG"; "YXOL"; "YTOG"; "RNPG"; "RXPL"; "YXPG"; "BXOG"; "BXOL"; "BTOG";
       "YXPL"; "RNPL"; "BCOG"; "YTPG"; "BTOL"; "RCOG"; "RXOG"; "YCPL"; "YNPL";
       "RNOL"; "BTPG"; "YCPG"; "BNPL"; "RXPG"; "BNOG"; "BNPG"; "RTOL"; "RTPG";
       "BXPL"; "RTPL"; "BNOL"; "RNOG"; "BCPG"; "BCPL"; "YTPL"; "YNOL"; "YTOL";
       "YCOL"; "RCOL"; "BTPL"]

    sort tiles 
