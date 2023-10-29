from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT, DATE, Boolean, true
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TableNameMixin


class Lexicon_ru(Base, TableNameMixin):
    """
    This class represents a User in the application.
    If you want to learn more about SQLAlchemy and Alembic, you can check out the following link to my course:
    https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126

    Attributes:
        user_id (Mapped[int]): The unique identifier of the user.
        username (Mapped[Optional[str]]): The username of the user.
        full_name (Mapped[str]): The full name of the user.
        active (Mapped[bool]): Indicates whether the user is active or not.
        language (Mapped[str]): The language preference of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.

    Inherited Attributes:
        Inherits from Base, TimestampMixin, and TableNameMixin classes, which provide additional attributes and functionality.

    Inherited Methods:
        Inherits methods from Base, TimestampMixin, and TableNameMixin classes, which provide additional functionality.

    """
    text_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    content: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"

class Lexicon_Menu(Base, TableNameMixin):
    """
    This class represents a User in the application.
    If you want to learn more about SQLAlchemy and Alembic, you can check out the following link to my course:
    https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126

    Attributes:
        user_id (Mapped[int]): The unique identifier of the user.
        username (Mapped[Optional[str]]): The username of the user.
        full_name (Mapped[str]): The full name of the user.
        active (Mapped[bool]): Indicates whether the user is active or not.
        language (Mapped[str]): The language preference of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.

    Inherited Attributes:
        Inherits from Base, TimestampMixin, and TableNameMixin classes, which provide additional attributes and functionality.

    Inherited Methods:
        Inherits methods from Base, TimestampMixin, and TableNameMixin classes, which provide additional functionality.

    """
    text_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    content: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"


class Lexicon_KB(Base, TableNameMixin):

    text_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    content: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"