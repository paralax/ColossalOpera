FOOFILES=anagram_detector.md concatenated_ints.md

foo.pdf: foo.tex
	cat header.tex foo.tex footer.tex > foo2.tex
	pdflatex -shell-escape foo2.tex

foo.tex: foo.md
	pandoc foo.md --latex-engine=xelatex -o foo.tex

foo.md:
	@echo $(FOOFILES)
	$(foreach f,$(FOOFILES), cat $(f) >> foo.md; echo "" >> foo.md;)

clean:
	rm -f foo.*
	rm -f foo2.tex

# TODO
# - write some code to produce pretty solutions
# - book, chapters, sub-chapters
# - fonts
