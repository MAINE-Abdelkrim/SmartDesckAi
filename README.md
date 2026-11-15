# SmartDesk AI

**Intelligent Customer Support & Ticket Management Platform**

## Project Overview
SmartDesk AI is an academic engineering project that demonstrates professional software development, AI engineering, data science, and MLOps competencies. The platform will eventually provide user management, ticket handling, AI‑assisted classification, sentiment analysis, priority estimation, similarity search, and analytics.

## Technology Stack
- **Frontend**: React, TypeScript, Vite, Tailwind CSS, Recharts, Axios, React Router, React Hook Form, Zod
- **Backend**: Python 3.11+, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, JWT
- **ML / Data Science**: Pandas, NumPy, scikit‑learn, spaCy/NLTK, Sentence Transformers, Joblib
- **MLOps**: MLflow, DVC, Evidently (optional)
- **DevOps**: Docker, Docker‑Compose, GitHub Actions, SonarQube, Ruff, Black, Pytest

## Repository Structure
The full directory tree is described in `docs/project_structure.md`. Key top‑level sections:
- `src/` – core Python packages and backend service
- `frontend/` – React application
- `data/` – dataset placeholders
- `notebooks/` – exploratory notebooks
- `mlruns/` – MLflow experiment storage
- `docs/` – architecture and developer documentation
- `tests/` – unit, integration, and e2e test scaffolding

## Getting Started
1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd smartdesk-ai
   ```
2. **Setup environment**
   ```bash
   cp .env.example .env
   # edit .env with your local values
   ```
3. **Install dependencies**
   ```bash
   # Backend (Python)
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt

   # Frontend (Node)
   cd frontend
   npm install
   ```
4. **Run services**
   ```bash
   docker compose up --build
   ```
   This starts PostgreSQL, the FastAPI backend, the React frontend, and an MLflow tracking server.

5. **Run tests**
   ```bash
   pytest
   ```
6. **Code quality**
   ```bash
   ruff check .
   black --check .
   ```

## Contributing
Please read `docs/development_guide.md` for the Git workflow, branching model, and coding standards.

## License
MIT – see `LICENSE` for details.
