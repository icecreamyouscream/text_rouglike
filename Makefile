.PHONY: lint format

lint:
	ruff check . --output-format=pylint --fix
	mypy .

format:
	ruff format .