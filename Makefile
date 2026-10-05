.PHONY: lint format

lint:
	ruff check .
	mypy .

format:
	ruff format .