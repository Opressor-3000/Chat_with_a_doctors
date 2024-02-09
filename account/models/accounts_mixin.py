from sqlalchemy.orm import declared_attr, Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey, Integer
from .account import Account


class AccountListRelationMixin:
    _accounts_back_populate: str
    _accounts_lazy: str
    _accounts_uselist: bool
    _accounts_secondary: str | None = None

    @declared_attr
    def accounts(cls) -> Mapped[list[Account]]:
        return relationship(
            back_populates=cls._accounts_back_populate,
            secondary=cls._accounts_secondary,
            lazy=cls._accounts_lazy,
            uselist=cls._accounts_uselist,
        )


class AccountRelationMixin:
    _account_foreignkey_name: str
    _account_unique: bool = False
    _account_nullable: bool = True
    _account_onupdate: str = "CASCADE"
    _account_ondelete: str = "RESTRICT"
    _account_back_populate: str
    _account_lazy: str
    _account_uselist: bool
    _account_secondary: str | None = None

    @declared_attr
    def account_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer,
            ForeignKey(
                "account.id",
                ondelete=cls._account_ondelete,
                onupdate=cls._account_onupdate,
                name=cls._account_foreignkey_name,
            ),
            unique=cls._account_unique,
            nullable=cls._account_nullable,
        )
    
    @declared_attr
    def account(cls) -> Mapped[Account]:
        return relationship(
            'Account',
            back_populates=cls._account_back_populate,
            lazy=cls._account_lazy,
            uselist=cls._account_uselist,
            secondary=cls._account_secondary,
        )
