from contextlib import contextmanager
from typing import ContextManager
from typing import List

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


DB_URI = 'sqlite:///weather.db'

Base = declarative_base()


class City(Base):
    __tablename__ = 'City'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"City(id={self.id}, name={self.name})"


engine = create_engine(DB_URI, encoding='utf-8')
Base.metadata.create_all(engine)


@contextmanager
def session(**kwargs) -> ContextManager[Session]:
    new_session = Session(**kwargs, bind=engine, expire_on_commit=False)
    try:
        yield new_session
        new_session.commit()
    except:
        new_session.rollback()
        raise
    finally:
        new_session.close()


def get_cities(*,
               ids: List[int] = None) -> List[City]:
    with session() as s:
        if ids:
            return s.query(City).filter(
                City.id.in_(ids)
            ).all()

        return s.query(City).all()


def add_cities(*, name: str) -> None:
    if not name:
        return

    with session() as s:
        city = City(name=name)
        s.add(city)

def delete_cities(*, city_id: int) -> None:
    with session() as s:
        city = s.query(City).filter_by(id=city_id).first()
        s.delete(city)
