from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID

from main import Base

import uuid


class User(Base):
   __tablename__ = "user"

   user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

