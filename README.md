### ai-notes-api



A backend REST API for creating and managing notes, with built-in AI summarization powered by Groq's LLaMA 3.3 70B model. Built with FastAPI and PostgreSQL, and deployed on Railway.

## Features

- Create, read, and delete notes
- One-click AI summarization of any note via Groq's LLaMA 3.3 70B (Versatile)
- PostgreSQL persistence via SQLAlchemy ORM
- Environment-based configuration with `.env`
- Centralized error handling and logging
- Auto-generated interactive API docs (Swagger UI)

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| AI / LLM | Groq API (LLaMA 3.3 70B Versatile) |
| Config | python-dotenv |
| Deployment | Docker, Railway |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/notes/` | Create a new note |
| GET | `/notes/` | Get all notes |
| GET | `/notes/{id}` | Get a single note by ID |
| DELETE | `/notes/{id}` | Delete a note by ID |
| POST | `/notes/{id}/summarize` | Generate an AI summary for a note |

## Getting Started

### Prerequisites

- Python 3.10+
- A PostgreSQL database (local or hosted, e.g. Railway/Supabase)
- A Groq API key (console.groq.com)

### Installation

git clone https://github.com/antariksha-agi/ai-notes-api.git
cd ai-notes-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### Environment Variables

Create a `.env` file in the project root:

DATABASE_URL=postgresql://user:password@host:port/dbname
GROQ_API_KEY=your_groq_api_key_here

### Run Locally

uvicorn main:app --reload

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.


## Project Structure

.
├── main.py          # FastAPI app, routes, exception handling
├── models.py         # Pydantic schemas (request/response models)
├── database.py        # SQLAlchemy engine, session, and ORM model
├── services.py        # Business logic: CRUD + Groq summarization
├── requirements.txt
└── .env               # Local environment variables (not committed)

## Deployed by Railway
here is the link below --
              ai-notes-api-production.up.railway.app

## Known Limitations

- No authentication — all endpoints are public
- No pagination on `GET /notes/`
- No update (PUT/PATCH) endpoint yet

## Roadmap

- [ ] Add note update endpoint
- [ ] Add pagination and search/filtering
- [ ] Add API key or JWT-based authentication
- [ ] Add automated tests

## License

MIT
