from pydantic import BaseModel


class MessageRegister(BaseModel):
    user: str
    message: str