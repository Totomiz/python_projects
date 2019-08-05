import logging

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
    var = session.query(Video).filter(Video.g_path == genres_dict.get(typename)).limit(count).all()
    for v in var:
        print(typename, v)
    session.commit()
    print('sr==', var)
    # session.close()
    return var


def query_video_by_path_and_limit(g_path, count):
    session = DBSession()
    var = session.query(Video).filter(Video.g_path == g_path).limit(count).all()
    for v in var:
        print(g_path, v)
    session.commit()
    print('query_video_by_path_and_limit==', var)
    # session.close()
    return var


# 根据类型名,简单查找N条视频数据，不包含视频源，详细描述
def query_video_by_simple(typename, count):
    result_array = []
    session = DBSession()
    selet_cl = [Video.id, Video.title_cn, Video.title_en, Video.g_path, Video.poster,
                Video.subtitle,
                Video.actors,
                Video.director, Video.total, Video.obtain_id]
    var = session.query().with_entities(Video.id, Video.title_cn, Video.title_en, Video.g_path, Video.poster,
                                        Video.subtitle,
                                        Video.actors,
                                        Video.director, Video.total, Video.obtain_id).filter(
        Video.g_path == genres_dict.get(typename)).limit(
        count).all()
    for v in var:
        item_dict = {}
        for idx, val in enumerate(v):
            item_dict[selet_cl[idx].name] = val
        print(typename, v)
        result_array.append(item_dict)
    session.commit()
    print('sr==', var)
    session.close()
    return result_array


# 根据类型路径,简单查找N条视频数据，不包含视频源，详细描述
def query_video_by_path_simple(g_path, count):
    result_array = []
    session = DBSession()
    select_cl = [Video.id, Video.title_cn, Video.title_en, Video.g_path, Video.poster,
                 Video.subtitle,
                 Video.actors,
                 Video.director, Video.total, Video.obtain_id]
    var = session.query().with_entities(Video.id, Video.title_cn, Video.title_en, Video.g_path, Video.poster,
                                        Video.subtitle,
                                        Video.actors,
                                        Video.director, Video.total, Video.obtain_id).filter(
        Video.g_path == g_path).limit(
        count).all()
    for v in var:
        item_dict = {}
        for idx, val in enumerate(v):
            item_dict[select_cl[idx].name] = val
        print(g_path, v)
        result_array.append(item_dict)
    session.commit()
    print('sr==', var)
    session.close()
    return result_array


def query_detail_video_by_obtain_id(obtain_id):
    session = DBSession()
    var = session.query(Video).filter(Video.obtain_id == obtain_id).first()
    print('first', var)
    session.commit()
    # session.close()
    return var


# 获取所有genres
def query_all_genres():
    res = []
    session = DBSession()
    var = session.query(Genres).all()
    for v in var:
        print("genres query:", v)
        res.append(v._asdict())
    session.commit()
    session.close()
    return res


def get_all_genres():
    sr = query_all_genres()
    print('sr==', sr)
    return sr


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
