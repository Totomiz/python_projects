import logging

from www.dbconnector import DBSession, genres_dict, Genres, Video


def init_genres():
    g_list = []
    for k, v in genres_dict.items():
        g_list.append(Genres(name=k, path=v))
    session = DBSession()
    session.add_all(g_list)
    session.commit()
    session.close()


# init_genres()


def query_video_index(index):
    session = DBSession()
    var = session.query(Video).filter(Video.g_path == genres_dict.get('电视剧')).limit(index)
    for v in var:
        logging.info('query_video_index:', v)
    session.commit()
    session.close()


def query_video_all():
    session = DBSession()
    var = session.query(Video).all()
    print('all size()->', len(var))
    session.commit()
    session.close()


def query_video_first():
    session = DBSession()
    var = session.query(Video).first()
    print('first', var)
    session.commit()
    session.close()


def query_video_all_movie(type):
    session = DBSession()
    var = session.query(Video).filter(Video.g_path == genres_dict.get(type))
    for v in var:
        print(type, v)
    session.commit()
    session.close()


# query_video_index(5)
# query_video_all()
# query_video_all_movie('纪录片')

if __name__ == "__main__":
    while True:
        v1 = input('输入查询数量：')
        query_video_index(v1)
