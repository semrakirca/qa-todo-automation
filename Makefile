install:
	python -m pip install -r requirements.txt
	python -m playwright install

smoke:
	pytest -v -m smoke --html=report.html --self-contained-html

regression:
	pytest -v -m regression --html=report.html --self-contained-html

all:
	pytest -v --html=report.html --self-contained-html
