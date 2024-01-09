from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT, DATE, Boolean, true
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TableNameMixin


class Lexicon_Ru(Base, TableNameMixin):
    text_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    content: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"


class Lexicon_KB(Base, TableNameMixin):
    text_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    content: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"
    

class Lexicon_Admin(Base, TableNameMixin):
    text_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    content: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"