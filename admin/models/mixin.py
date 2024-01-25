from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship


from admin.models.permission import Permission


class CreaterRelationMixin:
   _creater_unique: bool = False
   _creater_back_populates: str | None = None
   _creater_id_nullable: bool = False

   @declared_attr
   def creater_id(cls) -> Mapped[int]:
      return mapped_column(ForeignKey("permission.id"), nullable=cls._creater_id_nullable, unique=cls._creater_unique)

   @declared_attr
   def creater(cls) -> Mapped["Permission"]:
      return relationship("Permission", back_populates=cls._creater_back_populates)