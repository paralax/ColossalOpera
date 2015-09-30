EASYFILES=anagram_detector.md concatenated_ints.md cellular_automata.md thue_morse.md

foo.pdf: foo.tex
	pdflatex -shell-escape foo.tex
	# do this twice because of the TOC
	pdflatex -shell-escape foo.tex

foo.tex: foo.md
	pandoc foo.md --latex-engine=xelatex -o temp.tex
	cat header.tex temp.tex footer.tex | python process.py > foo.tex

foo.md:
	@echo $(EASYFILES)
	$(foreach f,$(EASYFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" >> foo.md; echo "" >> foo.md;)

clean:
	rm -f foo.* texput.log
	rm -f temp.tex
	rm -rf _minted-foo

# TODO
# - book, chapters, sub-chapters
# - fonts
