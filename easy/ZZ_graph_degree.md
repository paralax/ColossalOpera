# Title

[2016-05-09] Challenge #266 [Easy] Basic Graph Statistics: Node Degrees

# Difficulty

Easy

# Tags

graph theory, graph theory!node, graph theory!edge, graph theory!adjacency matrix

# Description

In graph theory, the *degree* of a node is the number of edges coming into it or going out of it - how connected it is. For this challenge you'll be calculating the degree of every node. 

# Input Description

First you'll be given an integer, *N*, on one line showing you how many nodes to account for. Next you'll be given an undirected graph as a series of number pairs, *a* and *b*, showing that those two nodes are connected - an edge. Example:

    3 
    1 2
    1 3

# Output Description

Your program should emit the degree for each node. Example:

    Node 1 has a degree of 2
    Node 2 has a degree of 1
    Node 3 has a degree of 1

# Challenge Input

This data set is an social network of tribes of the Gahuku-Gama alliance structure of the Eastern Central Highlands of New Guinea, from Kenneth Read (1954). The dataset contains a list of all of links, where a link represents signed friendships between tribes. It was downloaded from [the network repository](http://networkrepository.com/soc_tribes.php). 

    16
    1 2
    1 3
    2 3
    1 4
    3 4
    1 5
    2 5
    1 6
    2 6
    3 6
    3 7
    5 7
    6 7
    3 8
    4 8
    6 8
    7 8
    2 9
    5 9
    6 9
    2 10
    9 10
    6 11
    7 11
    8 11
    9 11
    10 11
    1 12
    6 12
    7 12
    8 12
    11 12
    6 13
    7 13
    9 13
    10 13
    11 13
    5 14
    8 14
    12 14
    13 14
    1 15
    2 15
    5 15
    9 15
    10 15
    11 15
    12 15
    13 15
    1 16
    2 16
    5 16
    6 16
    11 16
    12 16
    13 16
    14 16
    15 16

# Challenge Output

    Node 1 has a degree of 8
    Node 2 has a degree of 8
    Node 3 has a degree of 6
    Node 4 has a degree of 3
    Node 5 has a degree of 7
    Node 6 has a degree of 10
    Node 7 has a degree of 7
    Node 8 has a degree of 7
    Node 9 has a degree of 7
    Node 10 has a degree of 5
    Node 11 has a degree of 9
    Node 12 has a degree of 8
    Node 13 has a degree of 8
    Node 14 has a degree of 5
    Node 15 has a degree of 9
    Node 16 has a degree of 9

# Bonus: Adjacency Matrix

Another tool used in graph theory is an *adjacency matrix*, which is an *N* by *N* matrix where each *(i,j)* cell is filled out with the degree of connection between nodes *i* and *j*. For our example graph above the adjacency matrix would look like this:

    0 1 1
    1 0 0
    1 0 0

Indicating that node 1 is connected to nodes 2 and 3, but nodes 2 and 3 do not connect. For a bonus, create the adjacency matrix for the challenge graph. 

# Scala Solution

    def degree(edges:String) = 
        edges.
          split("\n").
          map(_.split(" ").filter(_.length>0)).
          toSet.
          toList.
          flatten.
          groupBy(_.toString).
          mapValues(_.size)
    
    def adj_matrix(edges:String, n:Int):String = {
        val m = Array.ofDim[Int](n,n)
        val es = edges.
                   split("\n").
                   map(_.split(" ").filter(_.length>0)).
                   map(_.map(_.toInt))
        for (e <- es) { m(e(0)-1)(e(1)-1) = 1; m(e(1)-1)(e(0)-1) = 1 }
        m.map(_.mkString(" ")).mkString("\n")
    }

    def challenge(edges:String) = 
        degree(edges).foreach { kv => println(kv._1 + " has a degree of " + kv._2) }
    
    def bonus(edges:String, n:Int) = {
        challenge(edges)
        println(adj_matrix(edges, n))
    }

# Go Solution

    package main

    import (
    	"fmt"
    	"io/ioutil"
    	"os"
    	"strconv"
    	"strings"
    )

    func check(e error) {
    	if e != nil {
    		panic(e)
    	}
    }

    func main() {
    	bdata, err := ioutil.ReadFile(os.Args[1])
    	check(err)

    	data := string(bdata)
    	var nodes map[string]int
    	nodes = make(map[string]int)

    	// calcuate node degree
    	lines := strings.Split(data, "\n")
    	for _, line := range lines {
    		vals := strings.Split(line, " ")
    		if len(vals) == 2 {
    			nodes[vals[0]] = nodes[vals[0]] + 1
    			nodes[vals[1]] = nodes[vals[1]] + 1
    		}
    	}
    	i := 0
    	for k, v := range nodes {
    		fmt.Printf("Node %s has a degree of %d\n", k, v)
    		i = i + 1
    	}

    	// bonus adjacency matrix
    	adjm := make([][]string, i)
    	for n := range adjm {
    		adjm[n] = make([]string, i)
    		for m := range adjm[n] {
    			adjm[n][m] = "0"
    		}
    	}
    	for _, line := range lines {
    		vals := strings.Split(line, " ")
    		if len(vals) == 2 {
    			x, err := strconv.ParseUint(vals[0], 10, 32)
    			check(err)
    			y, err := strconv.ParseUint(vals[1], 10, 32)
    			check(err)
    			adjm[x-1][y-1] = "1"
    			adjm[y-1][x-1] = "1"
    			adjm[x-1][x-1] = "1"
    		}
    	}

    	for n := 0; n < i; n++ {
    		fmt.Printf("%q\n", strings.Join(adjm[n], " "))
    	}
    }
