from fastapi import APIRouter, Depends, HTTPException
from users.dependencies import get_current_user
from notes.dao import NoteDAO
from notes.scheme import SchemeNoteCreate, SchemeNoteResponse
from notes.spell_checker import check_spelling
from typing import List

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("/add", response_model=SchemeNoteCreate)
async def add_note(note_data: SchemeNoteCreate, current_user: dict = Depends(get_current_user)):
    spelling_errors = await check_spelling(note_data.content)
    if spelling_errors:
        raise HTTPException(
            status_code=400,
            detail=f"Обнаружены орфографические ошибки в содержимом: {', '.join(spelling_errors)}"
        )

    created_note = await NoteDAO.add_note(
        title=note_data.title,
        content=note_data.content,
        owner_id=current_user.id
    )

    return created_note


@router.get("/my", response_model=List[SchemeNoteResponse])
async def get_notes(current_user: dict = Depends(get_current_user)):
    notes = await NoteDAO.get_user_notes(owner_id=current_user.id)
    return notes
