.PHONY: lint format install build clean

lint:
	uv run ruff check games_project_Kotayeva/VD_games

format:
	uv run ruff format games_project_Kotayeva/VD_games

check: lint format

install:
	uv pip install -e .

build:
	uv build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

test:
	uv run ruff check games_project_Kotayeva/VD_games

help:
	@echo "Available commands:"
	@echo "  make lint    - Check code with ruff"
	@echo "  make format  - Format code with ruff"
	@echo "  make check   - Run both lint and format"
	@echo "  make install - Install package in development mode"
	@echo "  make build   - Build package"
	@echo "  make clean   - Clean build artifacts"
