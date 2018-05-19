# title

[2015-03-26] Challenge #207 [Bonus] Erdos Number Calculator

# Difficulty

Intermediate

# Tags

math, graph theory, Erdos

In honor of the 102nd birthday of the famous mathematician, a problem named after him. 

# Description

Paul Erdos (1913–1996) was an influential mathematician who spent a large portion of his later life writing papers with a large number of colleagues, working on solutions to outstanding mathematical problems. The idea of the Erdos number was originally created by the mathematician's friends as a tribute to his enormous output. However, in later years it gained prominence as a tool to study how mathematicians cooperate to find answers to unsolved problems. 

The Erdos number describes the "collaborative distance" between mathematician Paul Erdos and another person, as measured by authorship of mathematical papers. Erdos himself has a number of 0, anyone he co-authored a paper with has a number of 1, anyone they co-authored a paper with (without Erdos) has a number of 2, and so forth. 

Several studies have shown that leading mathematicians tend to have particularly low Erdos numbers. For example, only 134,007 mathematicians have an Erdos number, with a median value of 5. In contrast, the median Erdos number of Fields Medalists is 3. Only 7,097 (about 5%) of mathematicians with a collaboration path have an Erdos number of 2 or less.

For this challenge you'll be working with a small, toy database of Erdos and related publications and be asked to calculate the Erdos number for several authors. 

# Input Description

You'll be given 2 integers on the first line, *N* and *M*. *N* is the number of of papers in APA format showing authors, titles, journals, and the like; think of it as a mini database. *M* is the number of authors to identify the Erdos number for. Note that all of the names should be in the same format of last name, then first and middle initials. 

# Output 

Your program should emit the name of the mathematician and their Erdos number.

# Challenge Input

	7 4
    Thomassen, C., Erdos, P., Alavi, Y., Malde, P. J., & Schwenk, A. J. (1989). Tight bounds on the chromatic sum of a connected graph. Journal of Graph Theory, 13(3), 353-357.
    Burr, S., Erdos, P., Faudree, R. J., Rousseau, C. C., & Schelp, R. H. (1988). Some complete bipartite graph-tree Ramsey numbers. Annals of Discrete Mathematics, 41, 79-89.
    Burris, A. C., & Schelp, R. H. (1997). Vertex-distinguishing proper edge-colorings. Journal of graph theory, 26(2), 73-82.
    Balister, P. N., Gyori, E., Lehel, J., & Schelp, R. H. (2007). Adjacent vertex distinguishing edge-colorings. SIAM Journal on Discrete Mathematics, 21(1), 237-250.
    Erdos, P., & Tenenbaum, G. (1989). Sur les fonctions arithmetiques liees aux diviseurs consecutifs. Journal of Number Theory, 31(3), 285-311.
    Hildebrand, A., & Tenenbaum, G. (1993). Integers without large prime factors. Journal de theorie des nombres de Bordeaux, 5(2), 411-484.
    Balister, P. N., Riordan, O. M., & Schelp, R. H. (2003). Vertex-distinguishing edge colorings of graphs. Journal of graph theory, 42(2), 95-109.
	Schelp, R. H.
	Burris, A. C.
	Riordan, O. M.
	Balister, P. N.

# Challenge Output

	Schelp, R. H. 1
	Burris, A. C. 2
	Riordan, O. M. 2
	Balister, P. N. 2

# Notes

This challenge is a shameless rip off of [an existing programming challenge](http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110206). It was too good to pass up; I did, however, compile my own challenge inputs and outputs. 

A full list of Erdos publications is up [here](https://wwwp.oakland.edu/enp/pubinfo/).
	

# Scala Solution

uses scalax's graph modules to do the heavy lifting.

	import scalax.collection.mutable.Graph
	import scalax.collection.GraphPredef._, scalax.collection.GraphEdge._
	import scalax.collection.edge.Implicits._

	object Bonus207 {
	  def main(args: Array[String]): Unit = {
	    val pubs = """Thomassen, C., Erdos, P., Alavi, Y., Malde, P. J., & Schwenk, A. J. (1989). Tight bounds on the chromatic sum of a connected graph. Journal of Graph Theory, 13(3), 353-357.
            Burr, S., Erdos, P., Faudree, R. J., Rousseau, C. C., & Schelp, R. H. (1988). Some complete bipartite graph-tree Ramsey numbers. Annals of Discrete Mathematics, 41, 79-89.
            Burris, A. C., & Schelp, R. H. (1997). Vertex-distinguishing proper edge-colorings. Journal of graph theory, 26(2), 73-82.
            Balister, P. N., Gyori, E., Lehel, J., & Schelp, R. H. (2007). Adjacent vertex distinguishing edge-colorings. SIAM Journal on Discrete Mathematics, 21(1), 237-250.
            Erdos, P., & Tenenbaum, G. (1989). Sur les fonctions arithmetiques liees aux diviseurs consecutifs. Journal of Number Theory, 31(3), 285-311.
            Hildebrand, A., & Tenenbaum, G. (1993). Integers without large prime factors. Journal de theorie des nombres de Bordeaux, 5(2), 411-484.
            Balister, P. N., Riordan, O. M., & Schelp, R. H. (2003). Vertex-distinguishing edge colorings of graphs. Journal of graph theory, 42(2), 95-109."""
	    val cos = List("Balister, P. N.", "Riordan, O. M.", "Burris, A. C.", "Schelp, R. H.")	

	    def loop(pubs:List[String], sofar:List[List[String]]): List[List[String]] = {
	      pubs match {
	        case Nil     => sofar
	        case pub::xs => loop(xs, sofar ++ pub.replace("& ", "").split("\\(")(0).split(", ").grouped(2).map(_.mkString(", ").trim).toList.combinations(2).toList)
	      }
	    }
		val g = loop(pubs.split("\n").toList, List(List()).tail).
					map(x=>x(0)~x(1)).
					foldLeft[Graph[String,UnDiEdge]](Graph()){_+=_}
	    for (c <- cos) {
	      g.get("Erdös, P.") shortestPathTo g.get(c) match {
	        case None => println(c + " NO PATH FOUND")
	        case Some(path) => println(c + " " + path.length)
	      }
	    }
	  }
	}
