from datetime import datetime

from sqlalchemy import DateTime, Integer, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
   __abstract__ = True

   @declared_attr.directive
   def __tablename__(cls) -> str:
      return cls.__name__.lower()
   
   # @declared_attr
   # def foo(cls) -> Mapped["Model"]:
   #    return rel

   id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
   created_at: Mapped[datetime] = mapped_column(
      DateTime,
      default=datetime.utcnow(), 
      nullable=False
      )


   