from www.ApiDataConvert import success_wrap_data
from www.dbdao import *

main_types_item = [['Banner', 1, "某某干嘛了"], ['今日热点', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                   ['天线宝宝', 3, '这就是巨星']]
movie_types_item = ['Banner', '最近更新', '院线同步']


def get_genres():
    return '{}'.format(success_wrap_data(get_all_genres()))


def get_home_main():
    result_dict = {}
    genres = get_all_genres()
    result_dict['genres'] = genres
    dataList = []
    for idx, valueList in enumerate(main_types_item):
        data_item_dict = {}
        # item = query_video_by_simple('电视剧', 4)
        offset = 0
        if valueList[1] > 2:
            offset = 1
        item = query_video_by_slice('电视剧', idx * 4 + offset, idx * 4 + offset + 4 + offset)
        data_item_dict['name'] = valueList[0]
        data_item_dict['style'] = valueList[1]
        data_item_dict['message'] = valueList[2]
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
