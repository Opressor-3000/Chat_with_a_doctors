from datetime import datetime


from sqlalchemy.orm import Mapped


from core.models.base import Base



class Message(Base):
    chat_id:Mapped[int]
    user_chat: Mapped[int]
    text:Mapped[int]
    deleted_at:Mapped[datetime]
    user_deleted:Mapped[int]



class MessageStatus(Base):
    message_id:Mapped[int]
    chat_user:Mapped[int]
    status_id:Mapped[int]