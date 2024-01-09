from sqlalchemy import Column, String, Text, ARRAY, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.database.models import Events

from sqlalchemy import select
from .base import BaseRepo

from sqlalchemy.ext.asyncio import AsyncSession

class EventRepo(BaseRepo):
  async def getting_events(
        self,
        button_name: str
  ):
    events = await self.session.query(Events).filter(Events.button_name == button_name).all()
    return events




Base = declarative_base()

class EventRepo(Base):

  def __init__(self, session_factory, db_name):
    button_name = Column(String)
    button_text = Column(Text)
    event_description = Column(Text)
    event_photo = Column(ARRAY(String))
    # Другие столбцы вашей таблицы events

engine = create_engine('postgresql://postgres:19581964@localhost:5432/User_Data')
Session = sessionmaker(bind=engine)
session = Session()

# Выбираем все столбцы для примера
results = session.query(Event.button_name, Event.button_text, Event.event_description, Event.event_photo).filter(Event.button_name == 'event_2').all()
#results = session.query(Event.button_name, Event.button_text, Event.event_description, Event.event_photo).all()
for button_name, button_text, event_description, event_photo in results:
    print(f"button_name: {button_name}")
    print(f"button_text: {button_text}")
    print(f"event_description: {event_description}")
    print(f"event_photo: {event_photo}")