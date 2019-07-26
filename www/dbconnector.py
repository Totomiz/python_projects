import logging

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy.orm.session import *


# dialect+driver://username:password@host:port/database
def _engine_port(test, echo):
    if test:
        return sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost:3306/testpydb',
                                        encoding='utf-8',
                                        echo=echo)
    else:
        return sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost:3306/videodb',
                                        encoding='utf-8',
                                        echo=echo)


engine = _engine_port(True, True)
Base = declarative_base()
genres_dict = {'电视剧': '1,', '连续剧': '2,', '电影': '3,', '综艺': '4,', '教育': '5,', '音乐': '6,', '记录片': '7,', '动漫': '8,'}


class Video(Base):
    __tablename__ = 'video'
    id = Column(BigInteger, default=0, autoincrement=True, nullable=False)
    title_cn = Column(String(length=100), nullable=False)
    title_en = Column(String(length=100), nullable=True)
    total = Column(INTEGER, default=0, nullable=True)
    g_path = Column(String(length=100), nullable=True)
    director = Column(String(length=300), nullable=True)
    actors = Column(String(length=500), nullable=True)
    subtitle = Column(String(length=500), nullable=True)
    desc = Column(TEXT, nullable=True)
    obtain_id = Column(String(length=120), nullable=False, primary_key=True)
    poster = Column(String(length=100), nullable=True)
    sources = relationship("Sources")

    def __repr__(self):
        return "<Video(id={},title_cn={},title_en={},total={},g_path={},director={},actors={},subtitle={},desc={}," \
               "obtain_id={},poster={},sources={})>".format(self.id, self.title_cn, self.title_en, self.total,
                                                            self.g_path, self.director, self.actors, self.subtitle,
                                                            self.desc, self.obtain_id, self.poster, self.sources)


class Genres(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False, unique=True)
    path = Column(String(length=120), nullable=False, unique=True)


class Sources(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=True)
    src = Column(String(length=120), nullable=False)
    video_obtain_id = Column(String(length=120), ForeignKey('video.obtain_id'), nullable=False)
    video = relationship("Video", back_populates='sources')

    def __repr__(self):
        return "<Sources(id={},name={},src={},video_obtain_id={})>".format(self.id, self.name, self.src,
                                                                           self.video_obtain_id)


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)
# Base.metadata.create_all(engine)

DBSession = sessionmaker()
DBSession.configure(bind=engine)

logging.info('_____________dbconnector.py execute DB START______________')
logging.info(Video.__tablename__)
logging.info(Sources.__tablename__)
logging.info(Genres.__tablename__)
