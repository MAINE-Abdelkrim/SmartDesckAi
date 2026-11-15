# Makefile

# Variables
PYTHON=python
PIP=pip
NPM=npm

# Setup
install:
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	cd frontend && $(NPM) install

# Lint & Format
lint:
	ruff check .
	black --check .
	cd frontend && $(NPM) run lint

format:
	ruff format .
	black .
	cd frontend && $(NPM) run format

# Test
test:
	pytest
	cd frontend && $(NPM) run test

# Run services
run:
	docker compose up --build

# Stop services
stop:
	docker compose down
