ALGORITHM 	:= sa
DEBUG		:=
run:
	source ./env/bin/activate; \
	python main.py -a $(ALGORITHM) $(DEBUG)

prepare:
	python -m venv ./env

test_sa:
	source ./env/bin/activate; \
	python simulated_annealing.py

style:
	yapf -i *.py

flake8:
	flake8 *.py

type_hint:
	mypy *.py
