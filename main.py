from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import init_db, get_db
from models import Notecreate, Note
import services
import logging
import traceback

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "type": type(exc).__name__}
    )

@app.on_event("startup")
def startup_event():
    try:
        logger.info("Initializing database...")
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}", exc_info=True)
        raise

@app.post("/notes/", response_model=Note)
def create_note(note: Notecreate, db: Session = Depends(get_db)):
    try:
        logger.debug(f"Creating note: {note}")
        return services.create_note(db, note)
    except Exception as e: 
        logger.error(f"Error creating note: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/", response_model=list[Note])
def read_all_notes(db: Session = Depends(get_db)):
    return services.get_all_notes(db)

@app.get("/notes/{id}", response_model=Note)
def read_note(id: int, db: Session = Depends(get_db)):
    db_note = services.get_note(db, id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@app.delete("/notes/{id}")
def delete_note(id: int, db: Session = Depends(get_db)):
    db_note = services.get_note(db, id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    services.delete_note(db, id)
    return {"message": "Note deleted successfully"}

@app.post("/notes/{id}/summarize", response_model=Note)
def summarize_note(id: int, db: Session = Depends(get_db)):
    db_note = services.summarize_note(db, id)
    if db_note == "Note not found":
        raise HTTPException(status_code=404, detail="Note not found")
    else:
        return db_note