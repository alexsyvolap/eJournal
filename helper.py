import os
import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_mixins import ReprMixin, SmartQueryMixin, ActiveRecordMixin

Base = declarative_base()


class BaseModel(Base, SmartQueryMixin, ActiveRecordMixin, ReprMixin):
    __abstract__ = True
    __repr__ = ReprMixin.__repr__
    pass

#################### setup ORM ######################


db_file = os.path.join(os.path.dirname(__file__), 'test.sqlite')
engine = sa.create_engine('mysql://root:123@localhost:3306/m', echo=False) # False to force
session = scoped_session(sessionmaker(bind=engine))

BaseModel.set_session(session)


def log(msg):
    print('\n{}\n'.format(msg))
