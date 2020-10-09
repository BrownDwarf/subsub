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
