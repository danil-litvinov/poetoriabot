from typing import Optional

from sqlalchemy import String, ARRAY, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TableNameMixin

class Events(Base, TableNameMixin):
    button_name: Mapped[str] = mapped_column(String(24), primary_key=True, autoincrement=False)
    button_text: Mapped[str] = mapped_column(Text)
    event_description: Mapped[str] = mapped_column(Text)
    event_photo: Mapped[list] = mapped_column(ARRAY(String))

    def __repr__(self):
        return f"<Lexicon {self.text_name} {self.content[:10]}>"