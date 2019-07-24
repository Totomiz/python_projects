from random import Random

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import sessionmaker

# dialect+driver://username:password@host:port/database
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost:3306/testpydb', encoding='utf-8',
                                  echo=True)
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    m_title_cn = Column(String(length=100), nullable=False)
    m_title_en = Column(String(length=100), nullable=True)
    m_g_path = Column(String(length=100))
    m_director = Column(String(length=100))
    m_actors = Column(String(length=100))
    m_subtitle = Column(String(length=500))
    m_desc = Column(String(length=1000))
    m_obtain_id = Column(String(length=50))
    m_poster = Column(String(length=100))

    def __init__(self, *arg, **kw):
        self.m_title_cn = kw.get('m_title_cn',
                                 'Name_Cn={}ni{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_title_en = kw.get('m_title_en',
                                 'Name_En={}wo{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_g_path = kw.get('m_g_path', ',{},{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_director = kw.get('m_director',
                                 '导演_director,{},{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_actors = kw.get('m_actors', '演员_actors,{},{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_subtitle = kw.get('m_subtitle',
                                 '子标题_actors,{},{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_desc = kw.get('m_desc', '详情_desc,{},{}'.format(Random().randint(10, 10), Random().randint(10, 10)))
        self.m_obtain_id = kw.get('m_obtain_id',
                                  '编排ID_obtain_id,{},{}'.format(Random().randint(10, 10), Random().randint(10, 10)))

    def __str__(self):
        return ''.join(('%s:%s ' % item for item in self.__dict__.items()))

    def __repr__(self):
        return ''.join(('%s:%s ' % item for item in self.__dict__.items()))


# Base.metadata

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)
# Base.metadata.create_all(engine)


print('----------', Random().randint(111, 999))

DBSession = sessionmaker()
DBSession.configure(bind=engine)

print(Movie.__tablename__)

mvList = [Movie(m_title_cn='wo shi 1'), Movie(m_title_cn='wo shi 2'), Movie(m_title_cn='wo shi 3')]


def addMovie():
    see = DBSession()
    see.add_all(mvList)
    see.commit()
    for m in mvList:
        print("add-->", m)


addMovie()


def same():
    see = DBSession()
    # see.en

# @property
# def __repr__(self):
#     return "<Movie(title_cn='%s', title_en='%s', g_path='%s',director='%s',actors='%s',subtitle='%s',desc='%s'," \
#            "poster='%s')>" % (self.m_title_cn, self.m_title_en, self.m_g_path)
