from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint, ForeignKey

from core.models import Base
from .mixin import CreaterRelationMixin


class Group(CreaterRelationMixin, Base):
    _creater_back_populates = 'group'
    
    title:Mapped[str] = mapped_column(String(60), unique=True)
    is_active:Mapped[bool] = mapped_column(Boolean, default=True, server_default=True)
    

class AccessGroup(CreaterRelationMixin, Base):
    _creater_back_populates = 'accessgroup'

    group_id:Mapped[int] = mapped_column(ForeignKey('group.id', ondelete='RESTRICT'))
    access_id:Mapped[int] = mapped_column(ForeignKey('access.id', ondelete='RESTRICT'))

    group:Mapped['Group'] = relationship('Group', back_populates='group')
    access:Mapped['Access'] = relationship('Access', back_populates='access')

    __table_args__ = (UniqueConstraint('group_id', 'access_id', name='access_group_uc'))


class Access(Base):
    title:Mapped[str] = mapped_column(String(32), unique=True)
    parent_id:Mapped[int] = mapped_column(ForeignKey('accesse.id'), nullable=True)

    parent:Mapped['Access'] = relationship('Access', back_populates='permission', remote_side=[id])

    # добавить constrian что не может быть циклов 

