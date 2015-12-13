all: run


run:
	rm -rf temp_cluster
	python vcluster.py
	ls temp_cluster

clear:
	rm *.pyc
