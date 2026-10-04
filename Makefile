.PHONY: lint format

lint:
	ruff check . --output-format=concise
	mypy .

format:
	ruff format .