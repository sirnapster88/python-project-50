install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest test/

lint:
	uv run ruff check .

check:
	test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml