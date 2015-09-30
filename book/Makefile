FOOFILES=anagram_detector.md concatenated_ints.md cellular_automata.md 

book.pdf: book.tex
	pdflatex -shell-escape book.tex
	# do this twice because of the TOC
	pdflatex -shell-escape book.tex

book.tex: book.md
	pandoc book.md --latex-engine=xelatex -o temp.tex
	cat header.tex temp.tex footer.tex | python process.py > book.tex

book.md:
	@echo $(FOOFILES)
	$(foreach f,$(FOOFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" >> book.md; echo "" >> book.md;)

clean:
	rm -f book.*
	rm temp.tex
	rm -rf _minted-book

# TODO
# - chapters
# - fonts
