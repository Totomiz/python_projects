from www.ApiDataConvert import success_wrap_data
from www.dbdao import *

main_types_item = ['Banner', '今日热点', '热剧点播']
movie_types_item = ['Banner', '最近更新', '院线同步']


def get_genres():
    return '{}'.format(success_wrap_data(get_all_genres()))


def get_home_main():
    result_dict = {}
    genres = get_all_genres()
    result_dict['genres'] = genres
    dataList = []
    for name in main_types_item:
        data_item_dict = {}
        item = query_video_by_simple('电视剧', 4)
        data_item_dict['name'] = name
        data_item_dict['item'] = item
        dataList.append(data_item_dict)
    result_dict['channel'] = dataList
    return '{}'.format(success_wrap_data(result_dict))


def get_home_type(g_path):
    # result_dict = {}
    # genres = get_all_genres()
    # result_dict['genres'] = genres
    # dataList = []
    # for name in main_types_item:
    #     data_item_dict = {}
    #     item = query_video_by_path_and_limit(g_id, 4)
    #     data_item_dict['name'] = name
    #     data_item_dict['item'] = item
    #     dataList.append(data_item_dict)
    # result_dict['channel'] = dataList
    result_dict = {'item': query_video_by_path_simple(g_path, 4)}
    return '{}'.format(success_wrap_data(result_dict))


def get_detail(obtain_id):
    return '{}'.format(success_wrap_data(query_detail_video_by_obtain_id(obtain_id)))
