all: ms.pdf

%.pdf: %.tex
	#pdflatex $<
	#pdflatex $<
	#bibtex ms
	#pdflatex ms
	#pdflatex ms
	tectonic ms.tex
	mv ms.pdf final/
	cp ms.tex final/
	rm -rf *Notes.bib
	rm -rf *.log
	rm -rf *.bbl
	rm -rf *.aux
	rm -rf *.out
	rm -rf *.blg
	rm -rf *.dvi

	# Change the commit SHA below to whatever diff you want
	git show 80598a8:document/ms.tex > ms_old.tex
	# Run Latex Diff on the new versus old
	latexdiff ms_old.tex ms.tex > ms_diff.tex
	tectonic ms_diff.tex
	mv ms_diff.pdf final/
	rm ms_old.tex
	rm -rf ms_diff.tex
	rm -rf *Notes.bib
	rm -rf *.log
	rm -rf *.bbl
	rm -rf *.aux
	rm -rf *.out
	rm -rf *.blg
	rm -rf *.dvi
