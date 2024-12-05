from fastapi import APIRouter, Depends

from app.db import Message, get_db
from app.schemas.message import MessageRegister

router_message = APIRouter(prefix="/message", tags=["message"])

db = get_db()

@router_message.get("/")
def read_root():
    return {"message": "hello world!"}

@router_message.post("/")
def create_message(message: MessageRegister, db=Depends(get_db)):
    """
    Create a new message.

    This endpoint allows the creation of a new message in the database.

    Args:
        message (MessageCreate): The message data to be created.
        db (Session, optional): The database session dependency.

    Returns:
        dict: A dictionary containing a success message.
    """
    db.add(Message(user=message.user, message=message.message))
    db.commit()
    return {"message": "message added"}

@router_message.get("/all")
def read_messages(db=Depends(get_db)):
    """
    Fetch all messages.

    This endpoint fetches all messages from the database.

    Args:
        db (Session, optional): The database session dependency.

    Returns:
        dict: A dictionary containing a list of messages.
    """
    messages = db.query(Message).all()
    return {"messages": [{"id": msg.id, "user": msg.user, "message": msg.message} for msg in messages]}

@router_message.get("/{user_id}")
def read_message(user_id: int, db=Depends(get_db)):
    """
    Fetch a message.

    This endpoint fetches a message from the database by its ID.

    Args:
        user_id (int): The ID of the message to fetch.
        db (Session, optional): The database session dependency.

    Returns:
        dict: A dictionary containing the message data.
    """
    message = db.query(Message).filter(Message.id == user_id).first()
    return {"message": {"id": message.id, "user": message.user, "message": message.message}}