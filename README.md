# ai-notes-api
AI-Powered Notes API
A backend REST API for creating and managing notes, with built-in AI summarization powered by Groq's LLaMA 3.3 70B model. Built with FastAPI and PostgreSQL, containerized with Docker, and deployed on Railway.
Features
Create, read, and delete notes
One-click AI summarization of any note via Groq's LLaMA 3.3 70B (Versatile)
PostgreSQL persistence via SQLAlchemy ORM
Environment-based configuration with .env
Centralized error handling and logging
Auto-generated interactive API docs (Swagger UI)
Tech Stack
Layer
Technology
Framework
FastAPI
Database
PostgreSQL
ORM
SQLAlchemy
Validation
Pydantic
AI / LLM
Groq API (LLaMA 3.3 70B Versatile)
Config
python-dotenv
Deployment
Docker, Railway
API Endpoints
Method
Endpoint
Description
POST
/notes/
Create a new note
GET
/notes/
Get all notes
GET
/notes/{id}
Get a single note by ID
DELETE
/notes/{id}
Delete a note by ID
POST
/notes/{id}/summarize
Generate an AI summary for a note
Getting Started
Prerequisites
Python 3.10+
A PostgreSQL database (local or hosted, e.g. Railway/Supabase)
A Groq API key
Installation
Bash