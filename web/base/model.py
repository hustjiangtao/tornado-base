# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""Base model settings"""

import json
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy import func, inspect

from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.ext.declarative import declarative_base, declared_attr

from sqlalchemy.sql.expression import text

from ..settings import SETTINGS
from .utils import DateTimeEncoder


class DBMixin:
    """单个对象的数据库操作（curd）"""

    @classmethod
    def add(cls, **kwargs) -> int:
        """Create"""
        data = {k: v for k, v in kwargs.items() if hasattr(cls, k)}
        if not data:
            return 0
        model = cls(**data)
        # model = cls()
        # for k,v in data.items():
        #     setattr(model, k, v)
        with session_scope() as session:
            session.add(model)
        return model.id

    @classmethod
    def delete(cls, pk: int) -> int:
        """Delete"""
        with session_scope() as session:
            count = session.query(cls).filter_by(id=pk).delete()
        return count

    @classmethod
    def update(cls, pk: int, **kwargs) -> bool:
        """Update"""
        data = {getattr(cls, k): v for k, v in kwargs.items() if hasattr(cls, k)}
        if not data:
            return False
        with session_scope() as session:
            session.query(cls).filter_by(id=pk).update(data)
        return True

    @classmethod
    def get(cls, pk: int) -> dict:
        """Retrieve"""
        with session_scope() as session:
            model = session.query(cls).filter_by(id=pk).first()
        return model.to_dict() if model else {}

    @classmethod
    def count(cls) -> int:
        """Count"""
        with session_scope() as session:
            count = session.query(func.count(cls.id)).scalar()
        return count


class MetaModel(DBMixin):
    """Base meta setting for sql obj"""

    id = Column(Integer, primary_key=True, autoincrement=True, comment='记录ID')
    create_time = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    # update_time = Column(TIMESTAMP, nullable=False, server_default=func.now(), server_onupdate=func.now(), comment='更新时间')

    # create_time = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP()'), comment='创建时间')
    update_time = Column(TIMESTAMP, nullable=False,
                         server_default=text('CURRENT_TIMESTAMP() on update CURRENT_TIMESTAMP()'), comment='更新时间')

    @declared_attr
    def __tablename__(cls):
        """define table name, lower case with _ to split"""
        name = ''.join([f'_{x}' if x.isupper() and idx != 0 else x for idx, x in enumerate(cls.__name__)])
        return name.lower()

    @declared_attr
    def __table_args__(cls):
        return {'mysql_charset': 'utf8mb4', 'mysql_engine': 'InnoDB'}

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    @classmethod
    def all_fields(cls, include: list = None, exclude: list = None):
        """get all model attrs
        usage: query(*DemoModel.all_fields()).all()
        """
        if exclude is None:
            exclude = []
        if include and isinstance(include, (list, tuple)):
            r = [getattr(cls, x) for x in (c.name for c in cls.__table__.columns) if x in include and x not in exclude]
        else:
            r = [getattr(cls, x) for x in (c.name for c in cls.__table__.columns) if x not in exclude]
        return r

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def to_dict(self, include=None):
        """transform sql obj to dict
        :param include: (list, tuple), item to return, eg: include=['id', 'name']
        """
        if include and isinstance(include, (list, tuple)):
            result = {x: getattr(self, x) for x in include}
        else:
            result = self.columnitems
        return result

    def _asdict(self):
        """keep same with sqlalchemy.util._collections.KeyedTuple._asdict
        query(model.id, model.name).all() -> KeyedTuple
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def to_json(self):
        """transform sql obj to json"""
        return json.dumps(self.to_dict(), cls=DateTimeEncoder)


def get_engine():
    # mysqlclient
    # mysql = 'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4'.format(**MYSQL)
    return create_engine(SETTINGS["db"], encoding='utf8', echo=False)


BaseModel = declarative_base(cls=MetaModel)
# Session = sessionmaker(bind=get_engine())
Session = scoped_session(sessionmaker(bind=get_engine()))


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        # session.remove()
        pass
