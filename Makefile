install:
	uv sync

test:
	uv run pytest -v

format:
	uv run black .

lint:
	uv run ruff check .

all: install test
