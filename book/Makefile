EASYDIR=../easy/
INTDIR=../intermediate/
HARDDIR=../hard/

EASYFILES=$(wildcard $(EASYDIR)*)
INTFILES=$(wildcard $(INTDIR)*)
HARDFILES=$(wildcard $(HARDDIR)*)

PANDOCARGS=--variable sansfont=Arial --latex-engine=xelatex -f markdown -t latex


pdf: book.pdf

book.pdf: book.tex easy.tex int.tex hard.tex
	pdflatex -shell-escape book.tex
	makeindex book
	# do this thrice because of the TOC and tables
	pdflatex -shell-escape book.tex
	pdflatex -shell-escape book.tex

easy.tex: easy.md
	pandoc easy.md -o easytmp.tex $(PANDOCARGS)
	cat easytmp.tex | python process.py > easy.tex

int.tex: int.md
	pandoc int.md -o inttmp.tex $(PANDOCARGS)
	cat inttmp.tex | python process.py > int.tex

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
	rm -f easytmp.tex inttmp.tex hardtmp.tex easy.tex int.tex hard.tex
	rm -rf _minted-book
	rm -f book.idx book.ilg book.ind book.aux book.log book.out book.pdf book.pyg book.toc easy.md hard.md int.md texput.log
