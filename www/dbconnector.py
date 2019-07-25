import asyncio
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
    title_cn = Column(String(length=100), nullable=False)
    title_en = Column(String(length=100), nullable=True)
    total = Column(INTEGER, default=0, nullable=True)
    g_path = Column(String(length=100), nullable=True)
    director = Column(String(length=100), nullable=True)
    actors = Column(String(length=100), nullable=True)
    subtitle = Column(String(length=500), nullable=True)
    desc = Column(String(length=1000), nullable=True)
    obtain_id = Column(String(length=120), nullable=false)
    poster = Column(String(length=100), nullable=True)


class Genres(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    path = Column(String(length=120), nullable=false)

dict={'电视剧':'1,','连续剧':'2,','电影':'3,','综艺':'4,'}

def initGenres():
    see = DBSession()
    # for k v

    # def __init__(self, *arg, **kw):
    #     self.title_cn = kw.get('title_cn',
    #                              'Name_Cn={}ni{}'.format(Random().randint(10, 1000), Random().randint(10, 1000)))
    #     self.title_en = kw.get('title_en',
    #                              'Name_En={}wo{}'.format(Random().randint(10, 200), Random().randint(10, 200)))
    #     self.g_path = kw.get('g_path', ',{},{}'.format(Random().randint(10, 200), Random().randint(10, 200)))
    #     self.director = kw.get('director',
    #                              '导演_director,{},{}'.format(Random().randint(10, 200), Random().randint(10, 200)))
    #     self.actors = kw.get('actors',
    #                            '演员_actors,{},{}'.format(Random().randint(10, 200), Random().randint(10, 200)))
    #     self.subtitle = kw.get('subtitle',
    #                              '子标题_actors,{},{}'.format(Random().randint(10, 200), Random().randint(10, 200)))
    #     self.desc = kw.get('desc', '详情_desc,{},{}'.format(Random().randint(10, 200), Random().randint(10, 200)))
    #     self.obtain_id = kw.get('obtain_id',
    #                               '编排ID_obtain_id,{},{}'.format(Random().randint(10, 200), Random().randint(10, 200)))

    # def __repr__(self):
    #     return "<Movie(title_cn={}, title_en={})>" .format (self.title_cn, self.title_en)

    # def __str__(self):
    #     return "<User(name='%s')>" % (self.title_cn)

    # def __repr__(self):
    #     return "<User(name='%s')>" % (self.title_cn)


# Base.metadata

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)
# Base.metadata.create_all(engine)


print('----------', Random().randint(111, 999))

DBSession = sessionmaker()
DBSession.configure(bind=engine)

print(Movie.__tablename__)

mv1 = Movie(title_cn='wo shi 1')
mv2 = Movie(title_cn='wo shi 2')
mv3 = Movie(title_cn='wo shi 3')

print("---", mv1.title_cn, mv1)

mvList = [mv1, mv2, mv3]


def checkSame():
    see = DBSession()
    mv4 = Movie(title_cn='wo shi 4')
    mv5 = Movie(title_cn='wo shi 1')
    see.add(mv4)
    print('same-->mv4===', mv4)
    see.query(mv5)
    outUser = see.query(Movie).filter_by(title_cn='wo shi 4').first()
    outUser2 = see.query(Movie).filter_by(title_cn='wo shi 1').first()
    print('same-->out===', outUser)
    print('same-->', mv5 is outUser2)

    see.commit()
    see.close()


async def addMovie():
    see = DBSession()
    print("start --- add move")
    await asyncio.sleep(2)
    see.add_all(mvList)
    see.commit()
    see.close()
    # for mv in mvList:
    #     print("add-->", mv)
    print("end --- add move--end")
    checkSame()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(addMovie())


def same():
    see = DBSession()
    # see.en

# @property
# def __repr__(self):
#     return "<Movie(title_cn='%s', title_en='%s', g_path='%s',director='%s',actors='%s',subtitle='%s',desc='%s'," \
#            "poster='%s')>" % (self.title_cn, self.title_en, self.g_path)
