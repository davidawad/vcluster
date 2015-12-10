all: run


run:
	rm -rf temp
	python vcluster.py
	ls temp

clear:
	rm *.pyc
