.PHONY: lint format

lint:
	ruff check . --output-format=pylint
	mypy .

format:
	ruff format .