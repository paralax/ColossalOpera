EASYDIR=../easy/
INTDIR=../intermediate/
HARDDIR=../hard/

EASYFILES=$(wildcard $(EASYDIR)*.md)
INTFILES=$(wildcard $(INTDIR)*.md)
HARDFILES=$(wildcard $(HARDDIR)*.md)

PANDOCARGS=--variable sansfont=Arial --latex-engine=xelatex -f markdown -t latex

pdf: book.pdf
	
epub: book.epub

book.epub: epub.css title.txt easyintro.md easy.md intintro.md int.md hardintro.md hard.md
	pandoc --epub-stylesheet=epub.css -t epub3 -o book.epub title.txt easyintro.md easy.md intintro.md int.md hardintro.md hard.md

book.pdf: book.tex easyintro.tex easy.tex intintro.tex int.tex hardintro.tex hard.tex
	pdflatex -shell-escape book.tex
	makeindex book
	# do this thrice because of the TOC and tables
	pdflatex -shell-escape book.tex
	pdflatex -shell-escape book.tex
	
easyintro.tex: easyintro.md
	pandoc easyintro.md -o easyintro.tex $(PANDOCARGS)

easy.tex: easy.md
	pandoc easy.md -o easytmp.tex $(PANDOCARGS)
	cat easytmp.tex | python process.py > easy.tex

intintro.tex: intintro.md
	pandoc intintro.md -o intintro.tex $(PANDOCARGS)

int.tex: int.md
	pandoc int.md -o inttmp.tex $(PANDOCARGS)
	cat inttmp.tex | python process.py > int.tex

hardintro.tex: hardintro.md
	pandoc hardintro.md -o hardintro.tex $(PANDOCARGS)

hard.tex: hard.md
	pandoc hard.md -o hardtmp.tex $(PANDOCARGS)
	cat hardtmp.tex | python process.py > hard.tex

easy.md: $(EASYFILES)
	@echo $(EASYFILES)
	$(foreach f,$(EASYFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" | sed "s/^\[.*] //g" >> easy.md; echo "" >> easy.md;)

int.md: $(INTFILES)
	@echo $(INTFILES)
	$(foreach f,$(INTFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" | sed "s/^\[.*] //g" >> int.md; echo "" >> int.md;)

hard.md: $(HARDFILES)
	@echo $(HARDFILES)
	$(foreach f,$(HARDFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" | sed "s/^\[.*] //g" >> hard.md; echo "" >> hard.md;)

clean:
	rm -f easytmp.tex inttmp.tex hardtmp.tex easy.tex int.tex hard.tex hardintro.tex intintro.tex easyintro.tex
	rm -rf _minted-book
	rm -f book.idx book.ilg book.ind book.aux book.log book.out book.pdf book.epub book.pyg book.toc easy.md hard.md int.md texput.log
