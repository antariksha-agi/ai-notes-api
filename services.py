from models import Notecreate, Note
from database import Notemodel
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env from the script's directory
env_file = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_file)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)


def create_note(db, note : Notecreate):
    db_note = Notemodel(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_all_notes(db):
    return db.query(Notemodel).all()

def get_note(db, id: int):
    return db.query(Notemodel).filter(Notemodel.id == id).first()

def delete_note(db, id: int):
    db_note = db.query(Notemodel).filter(Notemodel.id == id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
        return True
    else:
        return False

def summarize_note(db, id: int):
    db_note = db.query(Notemodel).filter(Notemodel.id == id).first()
    if db_note:
        response = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": f"Summarize this: {db_note.content}"}],
            model="llama-3.3-70b-versatile"
        )
        db_note.summary = response.choices[0].message.content
        db.commit()
        db.refresh(db_note)
        return db_note
    else:
        return "Note not found"    