from sqlalchemy import select
from .base import BaseRepo

from sqlalchemy.ext.asyncio import AsyncSession


class LexiconRepo:
    def __init__(self, session_factory, db_name):
        self.session_factory = session_factory
        self.db_name = db_name
        self.lexicon_dict = None  # Глобальная переменная для хранения словаря

    async def read_lexicon_table(self):
        async with self.session_factory() as session:
            # Читаем таблицу 'lexicon'
            lexicon_data = (await session.execute(select(self.db_name))).scalars().all()

            # Генерируем словарь
            self.lexicon_dict = {item.text_name: item.content for item in lexicon_data}

    async def get_value_by_key(self, key):
        # Проверяем, есть ли уже словарь, иначе читаем таблицу
        if self.lexicon_dict is None:
            await self.read_lexicon_table()

        # Возвращаем значение по ключу или None, если ключ не найден
        return self.lexicon_dict.get(key)
