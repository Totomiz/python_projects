import logging

from www.ApiDataConvert import *

logging.basicConfig(level=logging.INFO)

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
    logging.info('query_video_index:{}'.format("logging.info"))
    session = DBSession()
    var = session.query(Video).filter(Video.g_path == genres_dict.get('电视剧')).limit(index)
    for v in var:
        print('\n')
        logging.info('query_video_index:{}'.format(v))
    session.commit()
    session.close()
    return var


def query_video_all():
    session = DBSession()
    var = session.query(Video).all()
    print('all size()->', len(var))
    session.commit()
    session.close()
    return var


def query_video_first():
    session = DBSession()
    var = session.query(Video).first()
    print('first', var)
    session.commit()
    session.close()
    return var


def query_video_all_movie(type):
    session = DBSession()
    var = session.query(Video).filter(Video.g_path == genres_dict.get(type))
    for v in var:
        print(type, v)
    session.commit()
    session.close()
    return var


def query_video_by_type_and_limit(typename, count):
    session = DBSession()
    var = session.query(Video).filter(Video.g_path == genres_dict.get(typename)).limit(count)
    for v in var:
        print(typename, v)
    session.commit()
    session.close()
    return var


def query_all_genres():
    va=None
    session = DBSession()
    var = session.query(Genres).all()
    for v in var:
        print("genres query:", v)
    session.commit()
    # session.close()
    va=var
    return va


def get_all_genres():
    sr = query_all_genres()
    st = success_wrap_data2(sr)
    return st


# query_video_index(5)
# query_video_all()
# query_video_all_movie('纪录片')

if __name__ == "__main__":
    # query_video_index(66)
    get_all_genres()
    result = query_video_by_type_and_limit('电影', 2)
    # st = success_wrap_data(result)
    # print('json=', st)
    # while True:
    #     v1 = input('输入查询数量：')
